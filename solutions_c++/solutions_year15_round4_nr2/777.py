/*************************************************************************
	> File Name: b.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2015年05月30日 星期六 22时35分54秒
 ************************************************************************/

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cassert>
// #pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
#define LL long long
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define MAXN 105
template <typename T> inline void checkMax(T &a, T b) {a = a>b?a:b;}
template <typename T> inline void checkMin(T &a, T b) {a = a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
const double eps = 1e-8;
int T, Cas = 1, N;

char impossbile[] = "IMPOSSIBLE";

double V, X;

struct Node {
    double R, C;
} a[MAXN];

void small_task() {
    if (N == 1) {
        if (fabs(a[1].C - X) <= eps) {
            double ans = V / a[1].R;
            printf("%.10lf\n", ans);
        } else {
            printf("%s\n", impossbile);
        }
    } else if (N == 2) {
        if (a[1].C - X > eps && a[2].C - X > eps) {
            printf("%s\n", impossbile);
        } else if (X - a[1].C > eps && X - a[2].C > eps) {
            printf("%s\n", impossbile);
        } else if (fabs(a[1].C - X) <= eps && fabs(a[2].C - X) <= eps) {
            double ans = V / (a[1].R + a[2].R);
            printf("%.10lf\n", ans);
        } else if (fabs(a[1].C - X) <= eps) {
            double ans = V / a[1].R;
            printf("%.10lf\n", ans);
        } else if (fabs(a[2].C - X) <= eps) {
            double ans = V / a[2].R;
            printf("%.10lf\n", ans);
        } else {
            double k = (X - a[1].C) / (a[2].C - X);
            double x = V / (1.0 + k);
            double ans = max(x / a[1].R, k * x / a[2].R);
            printf("%.10lf\n", ans);
        }
    }
}

void work() {
    scanf("%d %lf %lf", &N, &V, &X);
    for (int i = 1; i <= N; i ++) {
        scanf("%lf %lf", &a[i].R, &a[i].C);
    }
    printf("Case #%d: ", Cas ++);
    small_task();
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
