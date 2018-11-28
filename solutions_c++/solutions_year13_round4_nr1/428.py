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
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int N;
int64 f(int64 x){
	return x*(2*N-x+1)/2;
}
int M,from[1010],to[1010],p[1010],cnt[1010];
void solve(){
	scanf("%d %d",&N,&M);
	int64 ans=0;
	FOR(i,M)scanf("%d %d %d",&from[i],&to[i],&p[i]);
	FOR(i,M)ans+=f(to[i]-from[i])*p[i];
	for(int i=1;i<N;i++)cnt[i]=0;
	FOR(i,M)for(int j=from[i];j<to[i];j++)cnt[j]+=p[i];
//FOR(i,N-1)cout<<cnt[i];cout<<endl;
	while(1){
		int from=0;
		while(from<N&&!cnt[from])++from;
		if(from==N)break;
		int to=from;
		while(to<N&&cnt[to])++to;
//cout<<from<<" "<<to<<endl;
		int take=cnt[from];
		for(int i=from;i<to;i++)take=min(take,cnt[i]);
		ans-=f(to-from)*take;
		while(from<to){
			cnt[from]-=take;
			++from;
		}
	}
	cout<<ans<<endl;
}

main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){ 
    cout<<"Case #"<<c<<": ";
		solve();
  }
}
