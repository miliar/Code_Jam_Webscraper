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

double tian[1010];
double han[1010];
int n;

int judge(double a[], double b[]);
int judgee(double a[], double b[]);

int main() {
    //freopen("D-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int nn;
    scanf("%d", &nn);
    repp(ii, 1, nn) {
        scanf("%d", &n);
        repp(i, 0, n) tian[i] = han[i] = 2;
        for (int i = 0; i < n;)
            scanf("%lf", &tian[i++]);
        for (int i = 0; i < n;)
            scanf("%lf", &han[i++]);
        sort(tian, tian + n), sort(han, han + n);
        printf("Case #%d: %d %d\n", ii, judge(tian, han), n - judge(han, tian));
    }
    return 0;
}


int judge(double a[], double b[]) {
    int aBig = n - 1, bBig = n - 1, aTail = 0, bTail = 0;
    int cnt = 0;
    for (;aTail <= aBig;) {
        if (a[aTail] > b[bTail])
            aTail++, bTail++, cnt++;
        else if (a[aTail] < b[bTail])
            aTail++, bBig--;
        else {
            if (a[aBig]>b[bBig]) cnt++, aBig--, bBig--;
            else aTail++, bBig--;
        }
    }
    return cnt;
}
