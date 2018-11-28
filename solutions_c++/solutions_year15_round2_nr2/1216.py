/*
*
* solved by Ahmed Kamal
*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int> 
#define ii pair<int,int> 
#define vii vector< pair<int,int> > 

#define ALL(v)        ((v).begin()), ((v).end())
#define SZ(v)       ((int)((v).size()))
#define CLR(v, d)     memset(v, d, sizeof(v))
#define REP(i, n)   for(int i=0;i<(int)(n);++i)
#define LOOP(i,b, n)    for(int i=(b);i<(int)(n);++i)

#define sc(x) scanf("%d",&x)
#define DSC(x) int x; scanf("%d",&x)
#define DSC2(x,y) int x,y; scanf("%d %d",&x,&y)

#define PB  push_back
#define MP  make_pair
double const EPS = 2.22045e-016;
#define INF (1<<29)


typedef vector<double>    VD;
typedef vector<string>    VS;
void print_v(vi arr){
int n = SZ(arr);
  REP(i,n)
    if(i == n-1)
       printf("%d\n",arr[i] );
     else
      printf("%d ", arr[i]);
}

int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }

int cnt(int n){
  int ans = 0;
  REP(i,30){
    if(n & 1<< i)
      ans++;
  }
  return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
#endif
int arr[20][20];
DSC(ts);

REP(t,ts){
  DSC2(r,c); DSC(n);

  int global = INF;
  REP(i,(1<<r*c)+1){
    if(cnt(i) == n){
      int ans = 0;
      CLR(arr,0);
      REP(k,31){
        if(i & 1<<k ){
          // printf("%d %d    ",k/c,k%c );
          arr[k/c][k%c] = 1;
        }
      }
      // printf("\nfinish\n");
      // counting walls
      REP(m,r){
        REP(k,c){
          if(arr[m][k] == 1 ){
            if(m < r-1 && arr[m+1][k] == 1)
              ans++;
            if(k < c-1 && arr[m][k+1] == 1)
              ans++;
          }
        }
      }
      // printf("at  i = %d ans = %d\n",i,ans);
      global = min(ans , global);
    }
  }
  printf("Case #%d: %d\n",t+1,global );
}

return 0; 
}
