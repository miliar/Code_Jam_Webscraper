#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<list>
#include<queue>
#include<cmath>
#include<functional>
#include<algorithm>
#include<cassert>
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	int b,m[1000],n;
	rep(testcase,t){
		int ans=-1;
		cin>>b>>n;
		rep(i,b)cin>>m[i];

		if(b<n){
			long long lb=0,ub=1ll<<50;
			while(ub-lb>1){
				long long mid=(lb+ub)/2;
				long long cnt=0;
				rep(i,b){
					cnt+=1+mid/m[i];
				}
				if(cnt>=n)ub=mid;
				else lb=mid;
			}
			long long cnt=0;
			rep(i,b){
				n-=1+lb/m[i];
			}
			rep(i,b){
				if(ub%m[i]==0 && --n==0){
					ans=i+1;
					break;
				}
			}
		}else{
			ans=n;
		}
		assert(ans!=-1);
		cout<<"Case #"<<testcase+1<<": "<<ans<<endl;
	}
	return 0;
}