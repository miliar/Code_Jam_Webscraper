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


string check(int n,int a,int R,int P,int S){
  int p[1<<12]={},c[4]={};

  p[0] = a;

  for(int i=0;i<n;i++){
    for(int j=(1<<i)-1;j>=0;j--){
      if(p[j]==1){
	p[j*2] = 1; p[j*2+1] = 2;
      }
      if(p[j]==2){
	p[j*2] = 2; p[j*2+1] = 3;
      }
      if(p[j]==3){
	p[j*2] = 1; p[j*2+1] = 3;
      }
    }
  }

  for(int i=0;i<(1<<n);i++){
    c[p[i]]++;
  }

  string ans;
  
  if(c[1]==R && c[2]==S && c[3]==P){

    for(int i=0;i<(1<<n);i++){
      if(p[i]==1) ans += "R";
      if(p[i]==2) ans += "S";
      if(p[i]==3) ans += "P";
    }

    for(int i=0;i<n;i++){
      for(int j=0;j<(1<<n);j+=(2<<i)){
	if(ans.substr(j,(1<<i)) > ans.substr(j+(1<<i),(1<<i))){
	  for(int k=j;k<j+(1<<i);k++){
	    swap(ans[k],ans[k+(1<<i)]);
	  }
	}
      }
    }
  }

  if(ans=="") return "ZZZ";
  
  return ans;

}

void solve(){
  int n,r,p,s;
  string ans="ZZZ";
  
  scanf("%d%d%d%d",&n,&r,&p,&s);

  ans = min(ans,check(n,1,r,p,s));
  ans = min(ans,check(n,2,r,p,s));
  ans = min(ans,check(n,3,r,p,s));

  if(ans=="ZZZ") puts("IMPOSSIBLE");
  else printf("%s\n",ans.c_str());
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
