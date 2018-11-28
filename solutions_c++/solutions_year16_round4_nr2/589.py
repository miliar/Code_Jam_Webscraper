#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<iomanip>

using namespace std;

typedef long long ll;
typedef  double ld;


int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    cout<<"Case #"<<tc<<": ";
    int n, k; cin>>n>>k;
    vector<ld> v(n,0);
    for (int i=0; i<n; ++i)
      cin>>v[i];
    ld ans=0;
    sort(v.begin(), v.end());
    int kb=n-k;
    for (int i=0; i+kb<=n; ++i){
      vector<ld> u(k,0);
      int c=0;
      for (int j=0; j<n; ++j){
	if (j<i || j>=i+kb){
	  u[c]=v[j];
	  ++c;
	}
      }
      vector<vector<ld> > w(k,vector<ld>(k/2+1,0));
      w[0][0]=u[0];
      w[0][1]=1-u[0];
      for (int j=1; j<k; ++j){
	w[j][0]=w[j-1][0]*u[j];
	for (int h=1; h<k/2+1; ++h)
	  w[j][h]=w[j-1][h]*u[j]+w[j-1][h-1]*(1-u[j]);
      }
      ans=max(ans,w[k-1][k/2]);
    }
    cout<<setprecision(10)<<ans<<endl;
  }
  return 0;
}
