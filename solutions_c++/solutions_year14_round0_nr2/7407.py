/*
 * Author:  chlxyd
 * Created Time:  2014-4-12 21:56:13
 * File Name: B.cpp
 */
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<ctime>
using namespace std;
const double eps(1e-8);
typedef long long lint;
#define clr(x) memset( x , 0 , sizeof(x) )
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clrs( x , y ) memset( x , y , sizeof(x) )

double C, F, X;
int T;

int main() {
    freopen("b.out", "w", stdout);
    int T, ca = 1; 
    scanf("%d", &T);
    while (T--) {
        scanf("%lf%lf%lf", &C, &F, &X); 
        double ans = 1e100;
        double old = 0;
        rep (i, X) {
            double nans = X / (i * F + 2) + old; 
            ans = min(nans, ans);  
            old = C / (i * F + 2) + old;
        }
        printf("Case #%d: ", ca++);
        printf("%.7f\n", ans);
    }
    return 0;
}

