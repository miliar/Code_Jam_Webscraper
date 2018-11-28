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
  int n;
  int f[SIZE][SIZE];
  
  scanf("%d",&n);
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      scanf("%1d",f[i]+j);
    }
  }

  int ans = INF;
  
  for(int k=0;k<(1<<(n*n));k++){
    int c = 0;
    int p[4] = {};
    vector<int> vec;
    
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	if(f[i][j]==0 && k&(1<<(i*n+j))) c++;
	p[i] = p[i]*2 + (f[i][j]==1 || k&(1<<(i*n+j)));
      }
    }

    map<int,int> mm;
    
    for(int i=0;i<n;i++){
      vec.push_back(p[i]);
      mm[p[i]]++;
    }

    bool f = true;
    
    for(auto it=mm.begin();it!=mm.end();it++){
      if(__builtin_popcount(it->first) != it->second) f = false;
    }

    if(f==false) continue;
    
    sort(vec.begin(),vec.end());
    vec.erase(unique(vec.begin(),vec.end()),vec.end());

    int flag = 0;
    int sum = 0;
    
    for(int i=0;i<vec.size();i++){
      sum += __builtin_popcount(vec[i]);
      flag = flag | vec[i];
    }
    
    if(sum==n && flag+1==(1<<n)){
      ans = min(ans,c);
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
