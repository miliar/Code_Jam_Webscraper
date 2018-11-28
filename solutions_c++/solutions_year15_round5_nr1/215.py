#include<stdio.h>
#include<string.h>
#include<vector>
#define M 1000000
using namespace std;
vector<int> c[M + 222];
vector<int> V[M + 222];
int s[M + 222] , m[M + 222];
int bit[M + 222];
int n,T,tc,as,cs,rs,am,cm,rm,d;
void maximize(int &a,int b){
	if(a < b) a = b;
}
int ans;
void update(int x,int v){
	for(;x <= M ; x+=x&-x) bit[x]++;
}
int get(int x){
	int res = 0;
	for(;x > 0 ; x-=x&(-x)) res+=bit[x];
	return res;
}
void dfs(int u,int prev,int maxs,int mins){
	c[mins].push_back(maxs);
	for(int i = 0 ; i < V[u].size() ; i++){
		int v = V[u][i];
		if(v != prev) dfs(v , u , max(maxs,s[v]) , min(mins,s[v]));
	}
}
main(){	
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	while(T > 0){
		tc++;
		ans = 0;
		scanf("%d %d %d %d %d %d %d %d %d %d",&n,&d,&s[0],&as,&cs,&rs,&m[0],&am,&cm,&rm);
		for(int i = 0 ; i <= n ; i++)
			V[i].clear() ;
		for(int i = 0 ; i <= rs ; i++)	c[i].clear();
		memset(bit , 0 , sizeof bit);
		for(int i = 1 ; i < n ; i++)
			s[i] = (1ll*s[i - 1]*as + cs)%rs;
		for(int i = 1 ; i < n ; i++){
			m[i] = (1ll*m[i - 1]*am + cm)%rm;
			int x = m[i]%i;
			V[x].push_back(i);
			V[i].push_back(x);
		}
		dfs(0 , -1 , s[0] , s[0]);
		for(int i = rs ; i >= max(0 , rs - d) ; i--)
			for(int j = 0 ; j < c[i].size() ; j++)	update(c[i][j] , 1);
		maximize(ans , get(rs));
		for(int i = rs - d - 1 ; i >= 0 ; i--){
			for(int j = 0 ; j < c[i].size() ; j++)	update(c[i][j] , 1);
			maximize(ans , get(i + d));
		}
		printf("Case #%d: %d\n",tc,ans);
		T--;
	}
}
