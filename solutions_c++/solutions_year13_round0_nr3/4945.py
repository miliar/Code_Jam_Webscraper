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
VI v(1001,0) ; 
void init()
{
 
 for(int i = 0 ; i*i <= 1000 ; i++ )
 {
      int rev = 0 ; 
      int y = i ; 
      while( y )    
      rev = rev*10 + y%10 , y/=10 ; 
      
      if( rev == i )
      {
          int x = i*i ; 
          rev=0 ; 
          while(x) 
          rev = rev*10 + x%10 , x/=10 ;
          
          if( i*i == rev ) 
          v[i*i] = 1 ; 
      }
      
      
 }
 
 
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
        int A , B ; 
        A = GI ;
        B = GI ; 
        int res = 0 ; 
        for(int i = A ; i <= B ; i++ )
        if( v[i]  )
        res++ ;
            
        
        cout << "Case #" << z << ": " << res << endl ; 
            
       }
   return 0;
}

