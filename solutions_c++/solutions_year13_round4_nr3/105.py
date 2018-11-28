#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()

using namespace std;

typedef long long ll;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;


#define TASK "a"
int n;
int a[10000];
int b[10000];
int ans[10000];
int in[10000];
int ou[10000];
int was[10000];

vi ls[10000];
void add(int x, int y) {
    ls[y].pb(x);
    in[x]++;
    ou[y]++;
 //   cerr<<y<<" < "<<x<<endl;
}
int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {   
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < n; i++) {   
            scanf("%d", &b[i]);
        }
        for (int i = 0; i < n; i++) {
            ls[i].clear();
            was[i] = 0;
            in[i] = 0;
            ou[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (a[i] == a[j]) {
                    add(i, j);
                }
                if (b[i] == b[j]) {
                    add(j, i);
                }
            }
            for (int j = i - 1; j >= 0; j--) {
                if (a[j] == a[i] - 1) {
                    add(i, j);
                    break;
                }
            }
            for (int j = i + 1; j < n; j++) {
                if (b[j] == b[i] - 1) {
                    add(i, j);
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            bool can = true;
            for (int j = 0; j < n; j++) if (was[j] == 0) {
                if (in[j] == 0) {
                    ans[j] = i + 1;
                    was[j] = 1;
                    can = false;
         //           cerr<<"put "<<i + 1<<" to "<<j<<endl;
                    for (int k = 0; k < sz(ls[j]); k++) {
                        in[ls[j][k]]--;
                    }
                    break;
                }
            }
            assert(!can);
        }
        for (int i = 0; i < n; i++) {
            printf("%d%c", ans[i], " \n"[i + 1 == n]);
        }
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 