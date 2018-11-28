#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
const int BUF = 55;
const int INF = 1<<30;


int N;
int nLine;
int line[BUF * 2][BUF];

void read() {
    cin >> N;
    nLine = N * 2 - 1;
    for (int i = 0; i < nLine; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> line[i][j];
        }
    }
}


bool isValid(int nFilled, bool used[BUF * 2], int curr[BUF][BUF]) {
    
    // Check whether there's a matching line for each row
    bool curUsed[BUF * 2];
    for (int i = 0; i < nLine; ++i) curUsed[i] = used[i];

    int noMatchCnt = 0;
    
    for (int c = 0; c < N; ++c) {
        bool isOk = false;
        for (int i = 0; i < nLine; ++i) {
            if (curUsed[i]) continue;
            
            for (int r = 0; r < nFilled; ++r) {
                if (line[i][r] != curr[r][c]) {
                    goto _fail;
                }
            }

            // matching line exists
            isOk = curUsed[i] = true;
            break;
            
        _fail:;
        }

        // matching line does not exist
        if (!isOk) {
            ++noMatchCnt;
            if (noMatchCnt >= 2) {
                return false;
            }
        }
    }

    // Check whether each row is arrenged in increasing order
    for (int c = 0; c < N; ++c) {
        for (int r = 0; r + 1 < nFilled; ++r) {
            if (curr[r][c] >= curr[r + 1][c]) {
                return false;
            }
        }
    }

    return true;
}


bool rec(int nFilled, bool used[BUF * 2], int curr[BUF][BUF]) {
    
    if (!isValid(nFilled, used, curr)) {
        return false;
    }

    if (nFilled == N) {
        return true;
    }
    
    // Find minimum value among line
    vector<pair<int,int> > lineValId;
    for (int i = 0; i < nLine; ++i) {
        if (used[i]) continue;
        if (nFilled - 1 >= 0 && curr[nFilled - 1][0] >= line[i][0]) continue;
        lineValId.push_back(make_pair(line[i][0], i));
    }
    sort(lineValId.begin(), lineValId.end());
    
    for (int i = 0; i < lineValId.size(); ++i) {

        used[lineValId[i].second] = true;
        for (int c = 0; c < N; ++c) {
            curr[nFilled][c] = line[lineValId[i].second][c];
        }
        
        if (rec(nFilled + 1, used, curr)) {
            return true;
        }
        
        used[lineValId[i].second] = false;
    }
    
    return false;
}


void work(int cases) {
    bool used[BUF * 2] = {};
    int curr[BUF][BUF] = {};
    
    rec(0, used, curr);
    
    memset(used, 0, sizeof(used));
    bool matchedR[BUF] = {};
    for (int r = 0; r < N; ++r) {
        for (int i = 0; i < nLine; ++i) {
            if (used[i]) continue;
            
            for (int c = 0; c < N; ++c) {
                if (line[i][c] != curr[r][c]) goto _fail1;
            }
            
            matchedR[r] = used[i] = true;
            break;
            
        _fail1:;
        }
    }
    
    bool matchedC[BUF] = {};
    for (int c = 0; c < N; ++c) {
        for (int i = 0; i < nLine; ++i) {
            if (used[i]) continue;
            
            for (int r = 0; r < N; ++r) {
                if (line[i][r] != curr[r][c]) goto _fail2;
            }
            
            matchedC[c] = used[i] = true;
            break;
            
        _fail2:;
        }
    }


    cout << "Case #" << cases << ":";

    for (int r = 0; r < N; ++r) {
        if (!matchedR[r]) {
            for (int c = 0; c < N; ++c) {
                cout << ' ' << curr[r][c];
            }
            cout << endl;
        }
    }
    
    for (int c = 0; c < N; ++c) {
        if (!matchedC[c]) {
            for (int r = 0; r < N; ++r) {
                cout << ' ' << curr[r][c];
            }
            cout << endl;
        }
    }
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
