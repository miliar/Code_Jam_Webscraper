#include <vector>
#include <cstdio>
#include <iostream>
#include <string>

#define BUFSIZE 100000
typedef long long int LLI;

using namespace std;

string tag(int i) {
    static char buf[BUFSIZE];
    sprintf(buf, "Case #%d: ", i + 1);
    return string(buf);
}

bool rcheck(vector<vector<int> > &dat, vector<int> &cstate, vector<int> &rstate, int pos, int row, int siz) {
    if (rstate[row] >= 0) { return false; }

    for (int i = row + 1; i < siz; ++i) {
        if (rstate[i] >= 0) {
            for (int j = 0; j < siz; ++j) {
                if (dat[rstate[i]][j] < dat[pos][j]) { return false; }
            }
            break;
        }
    }
    
    for (int i = row - 1; 0 <= i; --i) {
        if (rstate[i] >= 0) {
            for (int j = 0; j < siz; ++j) {
                if (dat[rstate[i]][j] > dat[pos][j]) { return false; }
            }
            break;
        }
    }

    for (int i = 0; i < siz; ++i) {
        if (cstate[i] >= 0) {
            if (dat[cstate[i]][row] != dat[pos][i]) { return false; }
        }
    }
    return true;
}

bool ccheck(vector<vector<int> > &dat, vector<int> &cstate, vector<int> &rstate, int pos, int col, int siz) {
    if (cstate[col] >= 0) { return false; }

    for (int i = col + 1; i < siz; ++i) {
        if (cstate[i] >= 0) {
            for (int j = 0; j < siz; ++j) {
                if (dat[cstate[i]][j] < dat[pos][j]) { return false; }
            }
            break;
        }
    }
    
    for (int i = col - 1; 0 <= i; --i) {
        if (cstate[i] >= 0) {
            for (int j = 0; j < siz; ++j) {
                if (dat[cstate[i]][j] > dat[pos][j]) { return false; }
            }
            break;
        }
    }

    for (int i = 0; i < siz; ++i) {
        if (rstate[i] >= 0) {
            if (dat[rstate[i]][col] != dat[pos][i]) { return false; }
        }
    }
    return true;
}

bool doit(vector<vector<int> > &dat, vector<int> &cstate, vector<int> &rstate, int pos, int siz) {
    if (dat.size() == pos) { return true; }
    
    for (int i = 0; i < siz; ++i) {
        if (ccheck(dat, cstate, rstate, pos, i, siz)) {
            cstate[i] = pos;
            if (doit(dat, cstate, rstate, pos + 1, siz)) {
                return true;
            } else {
                cstate[i] = -1;
            }
        }
    }
    for (int i = 0; i < siz; ++i) {
        if (rcheck(dat, cstate, rstate, pos, i, siz)) {
            rstate[i] = pos;
            if (doit(dat, cstate, rstate, pos + 1, siz)) {
                return true;
            } else {
                rstate[i] = -1;
            }
        }
    }

    return false;
}

string format(vector<vector<int> > &dat, vector<int> &cstate, vector<int> &rstate, int siz) {
    string res = "";
    char buf[BUFSIZE];

    int noc = -1;
    int nor = -1;
    for (int i = 0; i < siz; ++i) {
        if (cstate[i] < 0) { noc = i; }
        if (rstate[i] < 0) { nor = i; }
    }

    if (noc >= 0 && !(nor >= 0)) {
        for (int i = 0; i < siz; ++i) {
            if (i != 0) { res += " "; }
            sprintf(buf, "%d", dat[rstate[i]][noc]);
            res += buf;
        }
    } else if (nor >= 0 && !(noc >= 0)){
        for (int i = 0; i < siz; ++i) {
            if (i != 0) { res += " "; }
            sprintf(buf, "%d", dat[cstate[i]][nor]);
            res += buf;
        }
    } else {
        return "error";
    }

    return res;
}
string solve(vector<vector<int> > &lis) {
    int siz = lis.front().size();
    vector<int> cstate(siz, -1);
    vector<int> rstate(siz, -1);

    doit(lis, cstate, rstate, 0, siz);
    
    return format(lis, cstate, rstate, siz);
}

int main(int argc, char *argv[]) {
    int num;
    cin >> num;

    for (int i = 0; i < num; ++i) {
        vector<vector<int> > lis;
        int s;
        cin >> s;
        int s2 = s * 2 - 1;
        for (int j = 0; j < s2; ++j) {
            vector<int> lis2;
            for (int k = 0; k < s; ++k) {
                int x;
                cin >> x;
                lis2.push_back(x);
            }
            lis.push_back(lis2);
        }
        cout << tag(i) << solve(lis) << endl;
    }
    return 0;
}
