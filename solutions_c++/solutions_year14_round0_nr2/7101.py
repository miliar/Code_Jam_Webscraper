/*
 * Author:  chlxyd
 * Created Time:  2014/4/12 20:09:21
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
int T ;
double c , f , x ;
int main(){
    freopen("B.out","w",stdout) ;
    scanf("%d" , &T ) ;
    repf( t , 1 , T ) {
        scanf("%lf %lf %lf" , &c , &f , &x ) ;
        double ans = 1e100 ;
        double v = 2 , now = 0 ;
        while ( true ) {
            double nowans = now + x / v ;
            if ( nowans <= ans ) ans = nowans ;
            else break ;
            now += c / v ;
            v += f ;
        }
        printf("Case #%d: %.10lf\n" , t , ans ) ;
    }
}

