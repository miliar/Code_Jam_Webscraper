#include<bits/stdc++.h>
#define int64 long long
#define sqr(x) (x)*(x)
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define rep(i,x,y) for(int i=(x);i<=(y);++i)
#define VI vector<int>
#define VI64 vector<int64>
#define VS vector<string>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VPII vector< PII >
#define SZ(x) ((int)(x).size())
#define N 1200
using namespace std;
const double pi=acos(-1);
int T,n,K,tim;
int sum[N],s[N],low[N],high[N];
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for(scanf("%d",&T);T--;){
		cerr<<T<<endl;
		scanf("%d%d",&n,&K);
		memset(s,0,sizeof(s));
		rep(i,1,n-K+1){
			scanf("%d",&sum[i]);
			if(i==1)continue;
			s[i+K-1]=s[i-1]+(sum[i]-sum[i-1]);
		}
		
		rep(i,1,K){
			low[i]=0;
			high[i]=0;
		}
		rep(i,K+1,n){
			int u=(i-1)%K+1;
			low[u]=min(low[u],s[i]);
			high[u]=max(high[u],s[i]);
		}
	/*	if(tim==64){
			rep(i,1,K)printf("%d %d\n",low[i],high[i]);
			puts("");
		}*/
		
		int ans=1e9,u=0;
		rep(i,1,K)u=min(u,low[i]);
		rep(d,u-100000,u+100000*100/K){
			int L=0,R=2000000,mid;
			while(L<=R){
				mid=(L+R)/2;
				//
				bool flag=0;
				int ll=0,rr=0;
				rep(i,1,K){
					if(d-low[i]>d+mid-high[i])flag=1;
					ll+=d-low[i];
					rr+=d+mid-high[i];
				}
				if(!flag && ll<=sum[1] && rr>=sum[1])R=mid-1;
				else L=mid+1;
			}
			ans=min(ans,R+1);
		}
		printf("Case #%d: %d\n",++tim,ans);
	}
}

