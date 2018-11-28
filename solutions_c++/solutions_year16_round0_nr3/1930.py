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

bool is_prime(ll x){

  for(ll i = 2;i*i<=x;i++){
    if(x%i==0) return false;
  }

  return true;
}

ll divitor(ll x){

  for(ll i = 2;i*i<=x;i++){
    if(x%i==0) return i;
  }

  return -1;
}

ll power(int k,int n,int M){
    if(n==0) return 1;
    if(n==1) return (ll)k;
    
    ll ret = power(k,n/2,M);
    
    ret=(ret*ret)%M;
    
    if(n%2==1)
        ret=(ret*k)%M;
    
    return ret;
}

void solve(){
  int N,J;
  set<ll> ss;

  scanf("%d%d",&N,&J);

  while(1){
    int dig[50];

    dig[0] = dig[N-1] = 1;
    for(int i=1;i<N-1;i++){
      dig[i] = rand()%2;
    }

    int g = 0;
    for(int i=0;i<N;i++){
      g*=2;
      g += dig[i];
    }

    if(ss.find(g)!=ss.end()){
      continue;
    }
    ss.insert(g);
    
    bool flag = true;
    ll ans[11];
    
    for(int k=2;k<=10;k++){
      bool f2 = false;
      
      for(int i=2;i<=1000;i++){
	
	int s = 0;
	
	for(int j=0;j<N;j++){
	  if(dig[j]==1){
	    s += power(k,j,i);
	  }
	}

	if(s%i==0){
	  f2 = true;
	  ans[k] = i;
	  break;
	}
      }

      if(f2==false){
	flag = false;
	break;
      }
    }

    if(flag){
      for(int j=0;j<N;j++){
	printf("%d",dig[N-j-1]);
      }

      for(int j=2;j<=10;j++){
	printf(" %lld",ans[j]);
      }

      printf("\n");
      J--;
    }

    if(J==0) break;
  }
}

int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: \n",i);

    solve();
  }
  
  return 0;
}
