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
int n , r , p , s;
int win(int a,int b){
	return (a - b + 3) % 3 == 1 ? a : b;
}
string merge(string a,string b){
	return a < b ? a + b : b + a;
}
void main2(){
	scanf("%d%d%d%d",&n,&r,&p,&s);
	vector<string> V[3];
	rep(i,0,r) V[0].pb("R");
	rep(i,0,p) V[1].pb("P");
	rep(i,0,s) V[2].pb("S");
	rep(i,0,n){
		vector<string> nV[3];
		if(sz(V[0]) + sz(V[1]) < sz(V[2]) || sz(V[2]) + sz(V[0]) < sz(V[1]) || sz(V[2]) + sz(V[1]) < sz(V[0])){
			puts("IMPOSSIBLE");
			return ;
		}
		int t = (sz(V[0]) + sz(V[1]) - sz(V[2])) / 2;
		rep(j,0,t){
			nV[1].pb(merge(V[0][V[0].size()-1] , V[1][V[1].size()-1]));
			V[0].pop_back();
			V[1].pop_back();
		}
		rep(j,2,3) rep(k,0,2) if(sz(V[j]) && sz(V[k])){
			while(sz(V[j]) && sz(V[k])){
				nV[win(j , k)].pb(merge(V[j][V[j].size()-1] , V[k][V[k].size()-1]));
				V[j].pop_back();
				V[k].pop_back();
			}
		}
		rep(j,0,3) if(sz(V[j])){
			puts("IMPOSSIBLE");
			return;
		}
		rep(j,0,3) V[j] = nV[j];
	}
	rep(i,0,3) if(sz(V[i])){
		printf("%s\n",V[i][0].c_str());
		return ;
	}
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

/*
4
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2
 */
