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
#define INF (1<<29)
#define rep(i,n) for(int i=0;i<(int)(n);i++)
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	int d,p[1000];
	cin>>t;
	rep(i,t){
		cin>>d;
		rep(j,d)cin>>p[j];
		int maxp=*max_element(p,p+d);
		int ans=maxp;
		for(int j=1;j<ans;j++){
			int lb=0,ub=maxp;
			while(ub-lb>1){
				int mid=(lb+ub)/2;
				int rem=j;
				rep(k,d){
					rem -= (p[k]+mid-1)/mid-1;
				}
				if(rem<0)lb=mid;
				else ub=mid;
			}
			ans=min(ans,ub+j);
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}