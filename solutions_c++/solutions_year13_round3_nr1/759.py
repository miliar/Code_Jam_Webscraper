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
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

bool boin[26];

int sum[1000001];
int rh[1000001];
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	boin['a'-'a']=true;
	boin['i'-'a']=true;
	boin['u'-'a']=true;
	boin['e'-'a']=true;
	boin['o'-'a']=true;
	int T;
	cin>>T;
	rep(i,T){
		memset(sum,0,sizeof(sum));
		string s;
		int n;
		cin>>s>>n;
		long long ans=0;
		int c=0;
		rep(j,s.size()){
			if(boin[s[j]-'a'])c=0;
			else c++;
			sum[j+1]=sum[j]+(c>=n);
		}
		c=0;
		for(int j=s.size()-1;j>=0;j--){
			if(boin[s[j]-'a'])c=0;
			else c++;
			rh[j]=c;
		}
		rep(j,s.size()){
			if(rh[j]>=n){
				ans += s.size()-(j+n-1);
			}else{
				int a=j+rh[j];
				int lb=a-1,ub=s.size();
				while(ub-lb>1){
					int m=(lb+ub)/2;
					if(0<sum[m+1]-sum[a])ub=m;
					else lb=m;
				}
				ans += s.size()-ub;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}