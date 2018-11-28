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
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nn;
    scanf("%d", &nn);
    repp(ii, 1, nn) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double now = 0.0, rate = 2.0;
        while(rate * (rate + f) * c / (rate * f) - x < eps) {
            now += c / rate;
            rate += f;
        }
        now += x / rate;
        printf("Case #%d: %.7f\n", ii, now);
    }
    return 0;
}
