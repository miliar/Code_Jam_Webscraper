/*
ID: akshitpoddar
PROG:
LANG: C++
*/
#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<bitset>
#include<fstream>
#include<set>
#include<map>

#include<algorithm>
#include<cmath>
using namespace std;


// Definitions

#define LL long long int
#define PB push_back
#define MP make_pair
#define PII pair<int,int>
#define VI vector<int>
#define VL vector<LL>
#define VII vector< vector<int> >
#define VLL vector< vector<LL> >
#define VP vector< PII >
#define S(a) scanf("%lld",&a)
#define St string
#define X first
#define Y second
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define GI ({int t;scanf("%d",&t); t;})
#define gcd(a,b) __gcd(a,b)
#define MOD 1000000007
void Print (int *arr, int sz)
{
    int i = 0;
        while (i < sz)
        {
                printf("%d ",arr[i++]);
        }
        printf("\n");
}

// Main Code

void init()
{


}

int solve()
{

   return 0;
}

int main()
{
       init();
       LL t;
       S(t);
       for( int z = 1 ; z <= t ; z++ )
       {
            int n , m ; 
            n = GI ; 
            m = GI ; 
            VII lawn( n , VI(m) ) ; 
            
            for(int i = 0 ; i < n ; i++ )
            for(int j = 0 ; j < m ; j++ )
            lawn[i][j] = GI ; 
            
            VI row(n , -1 ); 
            VI col(m , -1 );
            
            for(int i = 0 ; i < n ; i++ )
            for(int j = 0; j < m ; j++ )
            row[i] = max( row[i] , lawn[i][j] ) ; 
            
            for(int i =0 ; i < m ; i++ )
            for(int j = 0 ; j < n ; j++ )
            col[i] = max( col[i] , lawn[j][i] ) ; 
            
            VII res( n , VI(m,100) ) ; 
            // ROW operations 
            for(int i = 0 ; i < n  ; i++ )
            for(int j = 0 ; j < m ; j++ )
            res[i][j] = min( res[i][j] , row[i] ) ; 
            
            // COL operatiions 
            for(int i = 0 ; i < m  ; i++ )
            for(int j = 0 ; j < n ; j++ )
            res[j][i] = min( res[j][i] , col[i] ) ; 
            
            int flag = 1 ; 
            for(int i = 0 ; i < n ; i++ )
            for(int j = 0 ; j < m ; j++ )
            flag &= ( res[i][j] == lawn[i][j] ) ; 
            
            
            
            cout << "Case #" << z << ": " ; 
            if( flag ) 
            cout << "YES" << endl ; 
            else
            cout << "NO" << endl ;  
       }
   return 0;
}

