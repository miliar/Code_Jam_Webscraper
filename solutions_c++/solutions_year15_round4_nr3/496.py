#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int N;
unordered_map<string, int> hashc[2];
vector<string> ss[20];

int lan[20];

int minw = 99999999;


int curc = 0;
void addr(int l, int d) {
    for (int i = 0; i < ss[l].size(); ++i) {
        if (d > 0) {
            if (hashc[lan[l]][ss[l][i]] == 0 && hashc[1 - lan[l]][ss[l][i]] > 0)  ++curc;
        } else {
            if (hashc[lan[l]][ss[l][i]] <= -d && hashc[1 - lan[l]][ss[l][i]] > 0)  --curc;
        }

        hashc[lan[l]][ss[l][i]] += d;
    }
}

void dfs(int level) {
    if (level < N) {
        lan[level] = 0;
        addr(level, 1);
        dfs(level+1);
        addr(level, -1);

        lan[level] = 1;
        addr(level, 1);
        dfs(level+1);
        addr(level, -1);
    } else {
        int cou = curc;

        if (cou < minw) {
            minw = cou;
        }
    }
}

int main () {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        for (int i = 0; i < 20; ++i) {
            ss[i].clear();
        }
        hashc[0].clear();
        hashc[1].clear();
        minw = 99999999;
        curc = 0;

        cin >> N;

        lan[0] = 0;
        lan[1] = 1;

        for (int i = 0; i < N; ++i) {
            string s;
            scanf("\n");
            getline(cin, s);
            stringstream ssin(s);

            string ts;
            while (ssin >> ts) {
                ss[i].push_back(ts);
            }
        }

        for (int l = 0; l < 2; ++l) {
            addr(l, 1);    
        }


        dfs(2);


        printf("Case #%d: %d\n", tt, minw);
    }

    return 0;
}
