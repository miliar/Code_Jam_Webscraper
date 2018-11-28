#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 200

void solve(){
  int n,k;
  double p[SIZE];
  int f[SIZE] = {};
  
  scanf("%d%d",&n,&k);
  for(int i=0;i<n;i++){
    scanf("%lf",p+i);
  }

  for(int i=1;i<=k;i++){
    f[n-i] = 1;
  }

  double ans = 0;
  
  do{
    double y[SIZE][SIZE] = {};
    int t = 0;
    
    y[0][0] = 1;
    
    for(int i=0;i<n;i++){
      if(f[i]){
	for(int j=t;j>=0;j--){
	  y[t+1][j+1] += y[t][j] * p[i];
	  y[t+1][j] += y[t][j] * (1-p[i]);	  
	}
	t++;
      }
    }

    ans = max(ans,y[k][k/2]);
    
  }while(next_permutation(f,f+n));
  
  printf("%.10lf\n",ans);
}


int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: ",i);

    solve();
  }
  
  return 0;
}
