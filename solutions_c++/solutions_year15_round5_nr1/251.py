#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
vector<ll> g[1100000];
ll dad[1100000];
ll n,m;
ll s[1100000];
ll ind[1100000];
ll  ch[1100000];
ll re[1100000];
ll amin[1100000];
int cmp(ll a ,ll b ){
	return s[a] < s[b];
}
ll ct = 0;
ll remain;
int dfs(ll k){
	ct++;
	ch[k] = 1;
	for(int i = 0 ; i < g[k].size() ; i++ ){
		if( ch[g[k][i]] == 0 ){
			dfs(g[k][i]);
		}
	}
}
ll tree[1100000];
int up(ll k,ll x){
	k++;
	for( ; k <= n ; ){
		tree[k]+=x;
		k+=(k&(-k));
	}
}
ll que(ll k){
	k++;
	ll res = 0;
	for( ; k > 0 ; ){
		res += tree[k];
		k-=(k&(-k));
	}
	return res;
}
int update(ll k,ll x){
	up(k,x);
}
ll query(ll a,ll b){
	ll res = que(b);
	if( a > 0 ) res -= que(a-1);
	return res;
}
int dfs2(ll k){
	ch[k] = 1;
	remain--;
	ll tmp = query(re[k],re[k]);
	update(re[k],-tmp);
	for(int i = 0 ; i < g[k].size() ; i++ ){
		if( ch[g[k][i]] == 0 ){
			dfs2(g[k][i]);
		}
	}
}
int dfs3(ll k,ll minn){
	if( re[k] < re[minn] ) minn = k;
	amin[k] = minn;
	for(int i = 0; i< g[k].size() ; i++ ){
		dfs3(g[k][i],minn);
	}
}
int dfs4(ll k,ll x){
	ct++;
	for(int i = 0 ; i < g[k].size() ; i++ ){
		if( ch[g[k][i]] == 0 && re[g[k][i]] > re[x] ){
			dfs4(g[k][i],x);
		}
	}
}

int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e< t ; e++ ){
		scanf("%lld %lld",&n,&m);
		remain = 0;
		for(int i = 0 ; i < n ; i++ ){
			ch[i] = 0;
			g[i].clear();
			tree[i] = 0;
		}
		ll a,c,r;
		scanf("%lld %lld %lld %lld",&s[0],&a,&c,&r);
		for(int i = 1 ; i < n ; i++ ){
			s[i] = (s[i-1]*a+c)%r;
		}
		scanf("%lld %lld %lld %lld",&dad[0],&a,&c,&r);
		for(int i = 1 ; i < n ; i++ ){
			dad[i] = (dad[i-1]*a+c)%r;
		}
		dad[0] = -1;
		for(int i = 1 ; i < n ; i++ ){
			dad[i] %= i;
			g[dad[i]].push_back(i);
		}
		for(int i = 0 ; i < n ; i++ ){
			ind[i] = i;
		}
		sort(ind,ind+n,cmp);
		for(int i = 0 ; i <n ; i++ ) re[ind[i]] = i;
		for(int i = 0 ; i < n ; i++ ){
			ll x = ind[i];
			ct = 0;
			if( ch[x] == 0 ) dfs(x);
			update(i,ct);
			//printf("%lld %lld,%lld %lld, %lld\n",x,dad[x],ct,s[x],query(i,i));
		}
		dfs3(0,0);
		for(int i = 0 ; i < n ; i++ ){
			//printf("%d %lld\n",i,amin[i]);
		}
		//printf("\n");



		for(int i = 0 ; i < n ; i++ ) ch[i] = 0;
		ll left = n-1;
		remain = n;
		ll ans = 0;
		for(int k = n ; k > 0 ; k-- ){
			int x = ind[k];
			if( k < n && ch[x] == 0 ){
				ct = 0;
				dfs4(x,amin[x]);
				if( amin[x] != x ){
					update(re[amin[x]],-ct);
				}
				dfs2(x);
			}
			for(int i = 0 ; i < n ; i++ ){
				//printf("%d %lld, ",i,query(re[i],re[i]));
			}
			//printf("\n");

			ll right = k-1;
			for( ; left > 0 && s[ind[right]]-s[ind[left-1]] <= m ; left-- );
			ll cur = remain;
			if( left > 0 ){
				cur -= query(0,left-1);
			}
			if( cur > ans ) ans = cur;
			//printf("x %lld %lld\n",remain,cur);
		}
		printf("Case #%d: %lld\n",e+1,ans);
	}
}
