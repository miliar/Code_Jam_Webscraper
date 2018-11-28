/*
 * Author:  Eyelids
 * Created Time:  2014/4/12 22:50:08
 * File Name: A.cpp
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
int x[10][10], y[10][10];
set <int> A;

int main() {
    freopen( "A.in", "r", stdin );
    freopen( "A.out", "w", stdout );
    
    int T;
    cin >>T;
    int cas = 0;
    while ( T -- ) {
        int a, b;
        scanf( "%d", &a );
        for ( int i = 1; i <= 4; i ++ ) 
            for ( int j = 1; j <= 4; j ++ )
                scanf( "%d", &x[i][j] );
        scanf( "%d", &b );
        for ( int i = 1; i <= 4; i ++ )
            for ( int j = 1; j <= 4; j ++ )
                scanf( "%d", &y[i][j] );
      
        int ans = -1, sum = 0; 
        A.clear();
        for ( int i = 1; i <= 4; i ++ )
            A.insert( x[a][i] );
        
        for ( int i = 1; i <= 4; i ++ )     
            if ( A.find( y[b][i] ) != A.end() ) {
                if ( ans == -1 ) ans = y[b][i], sum = 1; else sum ++;
            }

        printf( "Case #%d: ", ++cas ); 
        if ( ans == -1 )
            cout <<"Volunteer cheated!"<<endl;
        else if ( sum == 1 ) 
            cout <<ans<<endl;
        else
            cout <<"Bad magician!"<<endl;

    }

    return 0;
}







