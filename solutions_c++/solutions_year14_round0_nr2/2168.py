//source here#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define  lc(x) (x<<1)
#define  rc(x) (lc(x)+1)
#define  PI    (acos(-1))
#define  EPS   1e-8
#define  MAXN  444
#define  MAXM  44444
#define  LL    long long
#define  ULL   unsigned long long
#define  INF   0x3fffffff
#define  pb    push_back
#define  mp    make_pair
#define  mod   1000000007
#define  lowbit(x) (x&(-x))

using namespace std;

int t, cas;
double a, b, c;

int main(){
    //freopen("read.in", "r", stdin);
    //freopen("ans.txt", "w", stdout);
    cin >> t;
    while(t --){
        scanf("%lf%lf%lf", &a, &b, &c);
        double rt = 2.0;
        double tim = 0.0;
        double ans = 1e100;
        for(int i = 1; i <= 1000000; i ++){
            ans = min(ans, tim + c / rt);
            tim += a / rt, rt += b;
        }
        printf("Case #%d: %.7lf\n", ++ cas, ans);
    }
}
