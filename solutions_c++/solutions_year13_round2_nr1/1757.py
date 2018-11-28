#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <limits.h>
//#include <sys/time.h>
//#include <time.h>
using namespace std;
#define ll long long
ll dp[105][1000005];
int main(void)
{
	int T;
	cin>>T;

	for(int _t=1;_t<=T;++_t){	
		
		ll N,A;
		cin>>A>>N;
		vector <ll> m;
		m.resize(N);
		ll mx=0;
		for(int i=0;i<N;++i){
			cin>>m[i];
		}
		sort(m.begin(),m.end());
		ll result=N;
		if(A!=1){
#if 0
		sort(m.begin(),m.end());
		for(int i=0;i<=N;++i)for(int j=0;j<1000002;++j)dp[i][j]=N+1;
		dp[0][A]=0;
		for(int i=0;i<N;++i){
			for(ll j=A;j<1000002;++j){
				if(dp[i][j]==N+1)continue;
				if(j>m[i]){
					ll nxt=min(1000001ll,j+m[i]);
					dp[i+1][nxt]=min(dp[i+1][nxt],dp[i][j]);
					// nxt=min(1000001ll,j+j-1);
					//dp[i+1][nxt]=min(dp[i+1][nxt],dp[i][j]+1);
				}else{
					ll nxt=j;
					int cnt=0;	
					while(nxt<=m[i]){
						nxt=min(1000001ll,nxt+nxt-1);
						++cnt;
					}
					dp[i+1][nxt]=min(dp[i+1][nxt],dp[i][j]+cnt);
				}
			}
		}
		for(int i=0;i<=N;++i){
			for(int j=A;j<=A+10;++j)cout<<dp[i][j]<<",";
			cout<<endl;
		}
		for(int i=0;i<=N;++i){
			for(int j=0;j<1000002;++j){
				result=min(result,dp[i][j]+N-i);
			}
		}
#endif
		ll add=0;
		ll cur=A;
		for(int i=0;i<N;++i){
			result=min(N-i+add,result);
			if(cur>m[i]){
				cur=min(1000001ll,m[i]+cur);
			}else{
				ll nxt=cur;
				int cnt=0;
				while(nxt<=m[i]){
					nxt=min(1000001ll,nxt+nxt-1);
					++cnt;
				}
				cur=nxt+m[i];
				add+=cnt;
			}
		}
		if(cur<=m[N-1])cerr<<"eer"<<endl;
		result=min(result,add);
		}else{
			result=N;
		}
		cout<<"Case #"<<_t<<": "<<result<<endl;;
		cerr<<"cerr:"<<_t<<endl;
	}
}


//	cout.setf(ios::fixed);

