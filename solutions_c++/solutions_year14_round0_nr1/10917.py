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
#include<stdio.h>
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
       for(int z = 1 ; z <= t ; z++ )
       {
               int row ; 
               row = GI ; 
               int arr[17] = {0} ; 
               
               for(int i = 0 ; i < 4; i++ )
               for(int j = 0 ; j < 4 ; j++ )
               {
                       int x; 
                       cin >> x ; 
                       if( row == i+1 )
                       arr[x]++ ;
               }
               cin >> row ; 
               
               for(int i = 0 ; i < 4; i++ )
               for(int j = 0 ; j < 4 ; j++ )
               {
                       int x; 
                       cin >> x ; 
                       if( row == i+1 )
                       arr[x]++ ;
               }
               int res = 0 ; 
               int pos = 0 ; 
               for(int i = 1 ; i < 17; i++ )
               if( arr[i] == 2 )
               res++ ,pos = i ;
               
               printf("Case #%d: ", z) ;
               if( res == 1 )
               cout << pos << endl ; 
               else if( res == 0 )
               cout << "Volunteer cheated!\n" ;
               else
               cout << "Bad magician!\n";
               
       }
       
       return 0 ; 
}
               
               
       
               
               
