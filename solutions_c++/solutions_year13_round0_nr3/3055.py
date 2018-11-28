/*
 * Author:  chlxyd
 * Created Time:  2013/4/13 18:16:21
 * File Name: C.cpp
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
int f[1100];
int T ;
int main(){
    freopen("C.out","w",stdout) ;
    scanf("%d" , &T ) ;
    f[0] = 1 ; f[1] = 1 ; f[4] = 1 ; f[9] = 1 ;
    f[121] = 1 ; f[484] = 1 ; 
    repf( i , 1 , 1000 ) f[i] += f[i-1] ;
    repf( t , 1 , T ) {
        int a , b ;
        scanf("%d %d" , &a , &b ) ;
        printf("Case #%d: %d\n" , t , f[b] - f[a-1] ) ; 
    }
}

