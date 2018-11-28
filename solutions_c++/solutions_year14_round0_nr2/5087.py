#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef  long long LL;          
const int N = 105;
const int M = 20005;
const int INF = 1000000007;
double c , f , x;
int main () {
    #ifndef ONLINE_JUDGE
        freopen ("input.txt" , "r" , stdin);                                           
        freopen ("output.txt" , "w" , stdout);
    #endif
    int t , cas = 0;
    scanf ("%d" , &t);
    while (t --) {
        scanf ("%lf %lf %lf" , &c , &f , &x);
        double ans = x / 2.0 , can = 2.0 , pre = 0;
        for (int i = 1 ; i <= x + 1 ; i ++) {
            ans = min (ans , pre + x / can);
            pre += c / can;
            can += f;
        }
        printf ("Case #%d: %.9f\n" , ++ cas , ans);
    }
    return 0;
}