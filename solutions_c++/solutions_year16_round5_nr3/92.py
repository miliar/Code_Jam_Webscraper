#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
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
const int N = 1505;
int T,n,S;
int x[N] , y[N] , z[N];
struct ele{
	int a , b;
	int dis;
	bool operator < (const ele&b) const{
		return dis < b.dis;
	}
};
vector<ele> V;
int fa[N];
#define sq(x) (x)*(x)
int dis(int a,int b){
	return sq(x[a] - x[b]) + sq(y[a] - y[b]) + sq(z[a] - z[b]);
}
int findfa(int x){
	return x == fa[x] ? x : fa[x] = findfa(fa[x]);
}
int sz;
void merge(int a,int b){
	int pa = findfa(a) , pb = findfa(b);
	if(pa != pb){
		fa[pb] = pa;
	}
}
db wk(){
	scanf("%d%d",&n,&S);
	rep(i,0,n) scanf("%d%d%d%*d%*d%*d",x + i , y + i , z + i);
	V.clear();
	rep(i,0,n) rep(j,i+1,n) V.pb(ele{i , j , dis(i , j)});
	sort(all(V));
	rep(i,0,n) fa[i] = i;
	rep(i,0,sz(V)){
		ele t = V[i];
		merge(t.a , t.b);
		if(findfa(0) == findfa(1))
			return sqrt(t.dis * 1.0);
	}
	return 0;
}

int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		cerr << i << endl;
		printf("Case #%d: %.10f\n",i ,wk());
	}
	return 0;
}
