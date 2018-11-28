#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<b;++i)
#define per(i,a,b) for(int i=b-1;i>=a;--i)
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
const double pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , P = 1e9 + 7;
int Pow(int x,ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%P)if(t&1)r=(ll)r*x%P;return r;}
void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}
int n , ans;
char s[5][5];
bool has[5][5];
bool OK;bool v1[5] , v2[5];
void DFS(int c){
	if(c == n) return;
	rep(i,0,n) if(!v1[i]){
		v1[i] = true;
		int cc = 0;
		rep(j,0,n) if(!v2[j] && has[i][j] == true){
			++cc;
			v2[j] = true;
			DFS(c + 1);
			v2[j] = false;
		}
		if(cc == 0){
			OK = false;
			return ;
		}
		v1[i] = false;
	}
}

bool ok(){
	OK = true;rep(i,0,n) v1[i] = v2[i] = false;
	DFS(0);
	return OK;
}

void dfs(int r,int c,int pp){
	if(r == n){
//		rep(i,0,n) rep(j,0,n) printf("%d%c",has[i][j] , " \n"[j + 1 == n]);
		if(ok()){
			if(pp < ans){
				ans = pp;
			}
		}
		return;
	}
	int nr = r , nc = c + 1;if(nc >= n) nc=0,nr++;
	dfs(nr , nc , pp);
	if(s[r][c] == '0'){
		has[r][c] = 1;
		dfs(nr , nc , pp + 1);
		has[r][c] = 0;
	}
}

void main2(){
	scanf("%d",&n);
	rep(i,0,n) scanf("%s",s[i]);
	ans = inf;rep(i,0,n) rep(j,0,n) has[i][j] = s[i][j] == '1';
	dfs(0 , 0 , 0);
	printf("%d\n",ans);
}
int T;
int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		printf("Case #%d: ",i);
		main2();
	}
	return 0;
}
