#include <bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define INF (0x3f3f3f3f)

#define SZ(x) ((int)((x).size()))
#define PB(x) push_back(x)
#define MEMSET(x,v) memset(x,v,sizeof(x))
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))

typedef long long LL;
typedef pair<int, int> PII; typedef pair<PII, int> PII2;

#define MAXN (205)

vector<string> sentences[MAXN];
int N;

void solve() {
    cin >> N;
    string s;
    getline(cin, s);
    map<string, set<int> > words;
    REP(i, N) {
        sentences[i].clear();
        getline(cin, s);
        istringstream iss(s);
        while (iss >> s) {
            sentences[i].PB(s);
            words[s].insert(i);
        }
    }

    int ans = INF;
    REP(i, 1<<N) {
        if ((i & 1) == 0 && (i & 2) == 2) {
            int cnt = 0;
            for (auto it = words.begin(); it != words.end(); it++) {
                set<int> &ss = it->second;
                int mm = 0;
                for (int v : ss) {
                    if (((1<<v) & i) == 0) {
                        mm |= 1;
                    } else {
                        mm |= 2;
                    }
                    if (mm == 3) break;
                }
                if (mm == 3) {
                    cnt++;
                }
            }
            ans = min(ans, cnt);
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    REP(t, T) {
        printf("Case #%d: ", t + 1);
        solve();
    }


    return 0;
}
