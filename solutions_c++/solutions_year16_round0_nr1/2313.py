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


int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){
    ll s = 0,n,w;
    
    scanf("%lld",&n);

    if(n==0){
      printf("Case #%d: INSOMNIA\n",i);
      continue;
    }

    for(int j=1;;j++){
      w = n*j;

      while(w>0){
	s |= 1 << (w%10);
	w/=10;
      }

      if(s == (1<<10)-1){
	printf("Case #%d: %lld\n",i,n*j);
	break;
      }
    }
  }
  
  return 0;
}
