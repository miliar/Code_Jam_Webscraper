#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)>(b)?(b):(a))
#define rep(i,initial_n,end_n) for(int (i)=(initial_n);(i)<(end_n);i++)
#define repp(i,initial_n,end_n) for(int (i)=(initial_n);(i)<=(end_n);(i)++)
#define reep(i,initial_n,end_n) for((i)=(initial_n);(i)<(end_n);i++)
#define reepp(i,initial_n,end_n) for((i)=(initial_n);(i)<=(end_n);(i)++)
#define eps 1.0e-9
#define MAX_N 500

using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef long long ll;
typedef unsigned long long ull;

int main() {
    int nn;
    //freopen("in.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &nn);
    repp(ii, 1, nn) {
        int n, tmp; bool a[20] = { false };
        scanf("%d", &n);
        rep(i, 0, 4) {
            if(i == n - 1)
                rep(j, 0, 4) {
                    scanf("%d", &tmp);
                    a[tmp] = true;
                }
            else
                rep(j, 0, 4) scanf("%d", &tmp);
        }
        int m, ans12;
        bool ans11 = false, ans2 = false;
        scanf("%d", &m);
        rep(i, 0, 4) {
            if(i == m - 1) {
                rep(j, 0, 4) {
                    scanf("%d", &tmp);
                    if(a[tmp]) {
                        if(!ans11) ans11 = true, ans12 = tmp;
                        else ans2 = true;
                    }
                }
            }
            else rep(j, 0, 4) scanf("%d", &tmp);
        }
        printf("Case #%d: ", ii);
        if(ans2) puts("Bad magician!");
        else if(ans11) printf("%d\n", ans12);
        else puts("Volunteer cheated!");
    }
    return 0;
}
