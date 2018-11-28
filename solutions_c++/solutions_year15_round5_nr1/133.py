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
#define N 1200000
using namespace std;
const double pi=acos(-1);
int Ans,bo[N],be[N],fa[N],s[N],id[N],n,ans,T,tim,D,cnt=0;
VI E[N];
void mkd(int s[]){
	int a,b,c;
	scanf("%d%d%d%d",&s[0],&a,&b,&c);
	rep(i,1,n-1)s[i]=(1ll*s[i-1]*a+b)%c;
}
void dfs(int x,int flag){
	cnt++;
	if(!bo[x])return;
	if(be[x]==flag)return;
	if(be[x]==0)ans++;
	else ans--;
	be[x]=flag;
	
	for(int i:E[x])dfs(i,flag);
}
void add(int x){
	bo[x]=1;
	if(x==0 || be[fa[x]]==1){
		dfs(x,1);
	}
}
void del(int x){
	dfs(x,0);
	bo[x]=0;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for(scanf("%d",&T);T--;){
		cerr<<T<<endl;
		scanf("%d%d",&n,&D);
		mkd(s);
		mkd(fa);
		rep(i,0,n-1)E[i].clear();
		rep(i,1,n-1){
			fa[i]=fa[i]%i;
			E[fa[i]].pb(i);
		}
		fa[0]=-1;
		rep(i,0,n-1)id[i]=i;
		sort(id,id+n,[&](const int x,const int y){
			return s[x]<s[y];
		});
		memset(bo,0,sizeof(bo));
		memset(be,0,sizeof(be));
		Ans=0;
		ans=0;
		cnt=0;
		int j=0;
		rep(i,0,n-1){
			while(j<n && s[id[j]]-s[id[i]]<=D){
				add(id[j]);
				j++;
			}
			Ans=max(Ans,ans);
			del(id[i]);
		}
		printf("Case #%d: %d\n",++tim,Ans);
	}
}

