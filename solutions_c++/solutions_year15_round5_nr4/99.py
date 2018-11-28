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
using namespace std;
const double pi=acos(-1);
map<int64,int64> M;
int64 a[12000],ans[1200];
int num0;
int va[120][12000],tim,T,P;
bool dfs(int64 last,int dep,map<int64,int64> M){
	int tot=0;
	for(auto i:M)va[dep][++tot]=i.fi;
	if(tot==1 && M[va[dep][1]]){
		dep--;
		printf("Case #%d: ",++tim);
		rep(i,1,num0)ans[++dep]=0;
		sort(ans+1,ans+dep+1);
		rep(i,1,dep)printf("%I64d ",ans[i]);
		puts("");
		return 1;
	}
	
	rep(i,1,tot){
		int64 x=va[dep][i];
		if(x<last || x==0)continue;
		bool flag=0;
		int j;
		if(x>0){
			for(j=1;j<=tot;++j){
				if(M[va[dep][j]+x]<M[va[dep][j]]){
					flag=1;
					break;
				}
				M[va[dep][j]+x]-=M[va[dep][j]];
			}
		}else{
			for(j=tot;j>=1;--j){
				if(M[va[dep][j]+x]<M[va[dep][j]]){
					flag=1;
					break;
				}
				M[va[dep][j]+x]-=M[va[dep][j]];
			}
		}
		if(!flag){
			map<int64,int64> tmp;
			for(auto i:M)if(i.se!=0)tmp[i.fi]=i.se;
			ans[dep]=x;
			if(dfs(x,dep+1,tmp))return 1;
		}
		if(x>0){
			for(j--;j>=1;--j)
				M[va[dep][j]+x]+=M[va[dep][j]];
		}else{
			for(j++;j<=tot;++j)
				M[va[dep][j]+x]+=M[va[dep][j]];
		}
	}
	return 0;
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	for(scanf("%d",&T);T--;){
		cerr<<T<<endl;
		scanf("%d",&P);
		M.clear();
		rep(i,1,P)scanf("%I64d",&a[i]);
		rep(i,1,P){
			int64 x;
			scanf("%I64d",&x);
			M[a[i]]=x;
		}
		num0=0;
		for(;;){
			bool flag=1;
			for(auto i:M)if(i.se%2)flag=0;
			if(!flag)break;
			num0++;
			for(auto &i:M)i.se/=2;
		}
		dfs(-1e18,1,M);
	}
}

