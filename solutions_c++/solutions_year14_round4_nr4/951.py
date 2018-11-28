#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <unordered_map>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define CLEAR(v) memset((v), 0, sizeof(v))
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define LL long long

unordered_map<string, int> pcount[5];
int worst;
int times;
int M, N;
string S[10];
int inserv[5];
vector<string> pref[10];


void bt(int i, int nodes) {
    if(i < M) {
        REP(n, N) {
            inserv[n]++;
            REP(j, SZ(pref[i])) {
                if(pcount[n][pref[i][j]] == 0) nodes++;
                pcount[n][pref[i][j]]++;
            }
            bt(i+1, nodes);
            REP(j, SZ(pref[i])) {
                pcount[n][pref[i][j]]--;
                if(pcount[n][pref[i][j]] == 0) nodes--;
            }
            inserv[n]--;
        }
    } else {
        REP(n, N) if(inserv[n] == 0) return;
        if(nodes > worst) worst = nodes, times = 1;
        else if (nodes == worst) times++;
    }
}
    

int main()
{
    int T;
    cin >> T;
    FOR(caso, 1, T+1) {
        cin >> M >> N;
        REP(i, M) {
            cin >> S[i];
            pref[i].clear();
        }
        
        REP(i, M) {
            REP(j, SZ(S[i])+1) {
                pref[i].PB(S[i].substr(0, j));
                // cout << pref[i][j] << " ";
            }
            // cout << endl;
        }
        
        worst = 0;
        times=0;
        
        REP(n, N) {
            inserv[n] = 0;
            pcount[n] = unordered_map<string, int>();
            REP(i, M) {
                REP(j, SZ(S[i])) {
                    pcount[n].insert(MP(pref[i][j], 0));
                }
            }
        }
        
        bt(0, 0);
        
        cout << "Case #" << caso << ": ";
        cout << worst << " " << times << endl;
    
    }    
    return 0;
}
