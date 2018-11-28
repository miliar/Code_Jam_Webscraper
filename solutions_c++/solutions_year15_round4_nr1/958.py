#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>

using namespace std;

#define FOR(k,a,b) for(int k=(a); k < (b); k++)
#define FORE(k,a,b) for(int k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define ALL(c) (c).begin(), (c).end()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define RANGE(lb, x, ub) ((lb) <= (x) && (x) < (ub))

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-10;


int R, C; 


bool hit(vector<string> &board, int row, int col, PII dir) {
    int d = 1;
    while(true) {
        int nr = row + d * dir.first, nc = col + d * dir.second;

        if(!RANGE(0, nr, R) || !RANGE(0, nc, C)) return false;

        if(board[nr][nc] != '.') return true;

        d++;
    }
}


int main()
{
    map<char, PII> dirs;
    dirs['^'] = make_pair(-1, 0);
    dirs['>'] = make_pair(0, 1);
    dirs['v'] = make_pair(1, 0);
    dirs['<'] = make_pair(0, -1);

    int T; cin >> T;
    REP(tcase, T) {
        cin >> R >> C;
        vector<string> board(R); REP(i, R) cin >> board[i];

        int res = 0;
        REP(row, R) {
            REP(col, C) {
                if(board[row][col] != '.') {
                    auto dir = dirs[board[row][col]];
                    
                    if(!hit(board, row, col, dir)) {
                        bool ok = false;
                        for(auto it: dirs) {
                            if(hit(board, row, col, it.second)) {
                                ok = true;
                                break;
                            }
                        }

                        if(ok) res++;
                        else {
                            printf("Case #%d: IMPOSSIBLE\n", tcase+1);
                            goto END;
                        }
                    }
                }
            }
        }

        printf("Case #%d: %d\n", tcase+1, res);
        END:;
    }

    return 0;
}
