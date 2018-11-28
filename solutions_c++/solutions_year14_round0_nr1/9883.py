#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <functional>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <utility>
#define REP(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define ForIt(it, ct) for (__typeof((ct).begin()) it = (ct).begin(); it != (ct).end(); it++)
#define mset(ct, v) memset(ct, v, sizeof ct);
#define pb push_back
#define mp make_pair
#define INF 1 << 30

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

set<int> arr;
vi res;

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    int tc;
    int x;
    int idx1, idx2;
    scanf("%d", &tc);
    REP (nc, 1, tc) {
        arr.clear();
        res.clear();
        printf("Case #%d: ", nc);
        scanf("%d", &idx1);
        idx1--;
        REP (i, 0, 3) {
            REP (j, 0, 3) {
                scanf("%d", &x);
                if (i == idx1) {
                    arr.insert(x);
                }
            }
        }
        scanf("%d\n", &idx2);
        idx2--;
        REP (i, 0, 3) {
            REP (j, 0, 3) {
                scanf("%d", &x);
                if (i == idx2) {
                    if (arr.find(x) != arr.end()) {
                        res.pb(x);
                    }
                }
            }
        }
        if (res.size() == 0) {
            printf("Volunteer cheated!");
        } else if (res.size() == 1) {
            printf("%d", res[0]);
        } else {
            printf("Bad magician!");
        }
        printf("\n");
    }
}
