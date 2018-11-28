#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cassert>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int N,A[20],B[20];
vi sol[1<<20];
bool found[1<<20];
void solve(){
	cin>>N;
	FOR(i,N)cin>>A[i];
	FOR(i,N)cin>>B[i];
	FOR(i,1<<N)sol[i].clear();
	int left[20],right[20];
	sol[0].clear();
	sol[0].resize(N);
	for(int taken=1;taken<(1<<N);taken++){
		int nr=__builtin_popcount(taken);
		FOR(i,N){
			left[i]=i?left[i-1]:0;
			if(taken&1<<i)left[i]=max(left[i],A[i]);
		}
		for(int i=N-1;i>=0;i--){
			right[i]=i+1<N?right[i+1]:0;
			if(taken&1<<i)right[i]=max(right[i],B[i]);
		}
		FOR(i,N)if(taken&1<<i){
			int _left=i?left[i-1]:0;
			int _right=i+1<N?right[i+1]:0;
			if(_left+1==A[i]&&_right+1==B[i]&&sol[taken-(1<<i)].size()){
				vi tmp=sol[taken-(1<<i)];
				tmp[i]=nr;
				if(!sol[taken].size()||tmp<sol[taken]){
					sol[taken]=tmp;
				}
			}
		}
//cout<<taken<<endl;
//FOR(i,sol[taken].size())cout<<sol[taken][i]<<",";cout<<endl;
	}
	vi &ans=sol[(1<<N)-1];
	FOR(i,N)cout<<ans[i]<<(i+1<N?" ":"");
	cout<<endl;
}

main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){ 
    cout<<"Case #"<<c<<": ";
		solve();
  }
}
