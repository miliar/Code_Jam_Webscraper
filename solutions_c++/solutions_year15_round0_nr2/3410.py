#include <iostream>
#include <algorithm>
#include <cmath>
#include <set>
#include <vector>
using namespace std;
#define ll long long
int T,d;
const int maxn = 1000+10;
ll p[maxn];
int main(){
  /*
Int min=inf
For j=1 to m {
_int bank=j
_For i=1 to n 
__bank+=(kaf x_i/j)
_min=min(min,bank)
}
Print min*/
  cin>>T;
  for(int t=0;t<T;t++){
    cin>>d;
    for(int i=0;i<maxn;i++)
      p[i]=0;
    for(int i=0;i<d;i++)
      cin>>p[i];
    sort(p,p+d);
    ll ans = 1e15;
    for(int j=1;j<=p[d-1];j++){
      ll cur = j;
      for(int i=0;i<d;i++)
	cur+=(p[i] + j -1)/j - 1;
      ans = min(ans,cur);
    }
    cout<<"Case #"<<t+1<<": "<<ans<<endl;
    
  }
  return 0;
}
