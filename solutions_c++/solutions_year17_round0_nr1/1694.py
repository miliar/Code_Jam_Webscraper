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
#define SIZE 10000

void solve(){
  bool pan[SIZE];
  char in[SIZE];
  int n,k;
  
  scanf("%s%d",in,&k);
  n = strlen(in);
  
  for(int i=0;i<n;i++){
    pan[i] = '+' == in[i];
  }

  int ans = 0;
  
  for(int i=0;i<n-k+1;i++){
    if(!pan[i]){
      for(int j=i;j<i+k;j++) pan[j] = !pan[j];
      ans++;
    }
  }

  for(int i=0;i<n;i++){
    if(!pan[i]){
      puts("IMPOSSIBLE");
      return;
    }
  }

  printf("%d\n",ans);
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
