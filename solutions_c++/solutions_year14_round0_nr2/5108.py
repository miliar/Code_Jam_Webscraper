#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define fi first
#define se second

double c, f, x;

int main() {
    freopen("B-large.in" , "r", stdin);
    freopen("outB.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        cin >> c >> f >> x;
        double ans = 0.0;
        double speed = 2.0;
        double tmp1 , tmp2;
        while (1) {
           tmp1 = ans + (x / speed);
           tmp2 = ans + (c / speed) + (x / (speed + f));
           if (tmp1 < tmp2) {
               ans = tmp1;
               break;
           }
           else ans = ans + (c / speed), speed += f;
        }
        printf("Case #%d: %.7f\n",cas++, ans);   
    }
    return 0;
}
