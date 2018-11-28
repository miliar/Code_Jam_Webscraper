#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <functional>
#include <cassert>
#include <ctime>
#include <chrono>
using namespace std;
typedef long long ll;
typedef pair<int,int> pr;
#define REP(i,m,n) for (int i=(m); i<(n); ++i)
#define RREP(i,m,n) for (int i=(m)-1; i>=n; --i)

int main()
{
#ifdef MICRO_LOCAL
    freopen("in.put", "r", stdin);
    chrono::time_point<chrono::high_resolution_clock> timer_start, timer_end;
    timer_start = chrono::high_resolution_clock::now();
#endif
/*----------------------------------------------------------------------------*/
    int T; scanf("%d", &T);
    int TT = T;
    while (T--) {
        char s[1001]; int c, len;
        scanf("%s", s); scanf("%d", &c);
        len = strlen(s);
        int to = len-c+1;
        int ans = 0;
        REP(i,0,to) {
            if (s[i] == '-') {
                ans++;
                REP(j,i,i+c) {
                    if (s[j] == '+') {
                        s[j] = '-';
                    } else {
                        s[j] = '+';
                    }
                }
            }
            //printf("[%s]\n", s);
        }
        bool f = true;
        REP(i,to,len) {
            if (s[i] == '-') {
                printf("Case #%d: IMPOSSIBLE\n", TT-T);
                f = false;
                break;
            }
        }
        if (f) {
            printf("Case #%d: %d\n", TT-T, ans);
        }
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
