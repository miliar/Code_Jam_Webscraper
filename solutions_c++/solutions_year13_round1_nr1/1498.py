#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<utility>
#define mp make_pair
#define pb push_back
#define all(a) (a).begin() , (a).end()
using namespace std;
typedef long long ll ;
typedef vector < int > vi;
int main(){
    freopen("input" , "r" , stdin);
    freopen("output" , "w" , stdout);
    int t; 
    cin >> t; 
    int test = 1;
    while( t -- ){
           ll r, t, cur; 
           cin >> r >> t;
           ll ans = 0;
           cur = r+1;
           while( true )  {
                  if( t - (cur*cur - r*r) < 0 )       
                      break;
                  t -= (cur*cur - r*r);
                  ans ++ ;
                  cur += 2;
                  r += 2;
           }
           printf("Case #%d: %lld\n",test, ans);
           test ++ ;
    }
    return 0;    
}
