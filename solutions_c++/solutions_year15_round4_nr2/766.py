#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<queue>
#include<set>
#include<map>
#include<cmath>


using namespace std;

typedef long double ld;

int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    int n; cin>>n;
    ld v, x;
    vector<ld> r(n,0), c(n,0);
    cin>>v>>x;
    for (int i=0; i<n; ++i)
      cin>>r[i]>>c[i];
    cout<<"Case #"<<tc<<": ";
    if (n==1){
      if (c[0]==x)
	cout<<setprecision(10)<<v/r[0]<<endl;
      else
	cout<<"IMPOSSIBLE"<<endl;
      continue;
    }
    ld ans;
    if (c[0]>c[1]){
      sort(c.begin(), c.end());
      ld hei=r[0];
      r[0]=r[1];
      r[1]=hei;
    }
    if (c[0]>x || c[1]<x){
      cout<<"IMPOSSIBLE\n";
      continue;
    }
    if (c[0]<x && c[1]>x){
      ld a=(v*x-c[1]*v)/(c[0]-c[1]);
      ld b=(v*x-c[0]*v)/(c[1]-c[0]);
      cout<<setprecision(10)<<max(a/r[0], b/r[1])<<endl;
      continue;
    }
    if (c[0]==x)
      ans=v/r[0];
    if (c[1]==x)
      ans=v/r[1];
    if (c[0]==x && c[1]==x)
      ans=v/(r[0]+r[1]);
    cout<<setprecision(10)<<ans<<endl;
  }
  return 0;
}
