#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;++i)
#define per(i,a,b) for(int i=b-1;i>=a;--i)
#define set(a,b) memset(a,b,sizeof(a))
#define de(x) cout << #x << " = " << x << endl
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef double db;
typedef pair<int, int> pii;
typedef vector<int> vi;
const db pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , mod = 1e9 + 7;
int Pow(int x, ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%mod)if(t&1)r=(ll)r*x%mod;return r;}
int T , n;

void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}
const int N = 1010;
int a[N] , vis[N];
vi g[N];

int dfs(int c){
	vis[c] = true;
	int r = 0;
	for(auto t : g[c]){
		if(vis[t]) continue;
		int tmp = dfs(t);
		r = max(r , tmp);
	}
	return r + 1;
}
int cc[N] , vis2[N];
void main2(){
	scanf("%d",&n);
	rep(i,0,n) g[i].clear();
	rep(i,0,n) scanf("%d",a + i) , --a[i] , g[a[i]].pb(i) , vis[i] = false;
	int cnt = 0;
	rep(i,0,n) if(!vis[i]){
		if(a[a[i]] == i){
			vis[i] = true;
			vis[a[i]] = true;
			cnt += dfs(i);
			cnt += dfs(a[i]);
		}
	}
	int cnt2 = 0;
	set(cc, 0);
	rep(i,0,n) if(!vis[i]){
		vi v;
		for(int j=1,c=i;;++j){
			if(vis2[c]){
				cnt2 = max(cnt2 , j - cc[c]);
				break;
			}
			v.pb(c);
			vis2[c] = true;
			if(vis[c]) break;
			vis[c] = true;
			cc[c] = j;
			c = a[c];
		}
		rep(i,0,sz(v)) vis2[v[i]] = false;
	}
	printf("%d\n",max(cnt , cnt2));
}

int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		printf("Case #%d: ",i);
		main2();
	}
	return 0;
}

