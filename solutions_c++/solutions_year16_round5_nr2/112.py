#include <bits/stdc++.h>
#define REP(a,b) for(int a=0; a<(b); ++a)
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define FWDS(a,b,c,d) for(int a=(b); a<(c); a+=d)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define ALL(a) (a).begin(), (a).end()
#define SIZE(a) ((int)(a).size())
#define VAR(x) #x ": " << x << " "
#define popcount __builtin_popcount
#define popcountll __builtin_popcountll
#define gcd __gcd
#define x first
#define y second
#define st first
#define nd second
#define pb push_back

using namespace std;

template<typename T> ostream& operator<<(ostream &out, const vector<T> &v){ out << "{"; for(const T &a : v) out << a << ", "; out << "}"; return out; }
template<typename S, typename T> ostream& operator<<(ostream &out, const pair<S,T> &p){ out << "(" << p.st << ", " << p.nd << ")"; return out; }

typedef long long int64;
typedef pair<int, int> PII;
typedef long double K;
typedef vector<int> VI;

const int dx[] = {0,0,-1,1}; //1,1,-1,1};
const int dy[] = {-1,1,0,0}; //1,-1,1,-1};

vector<int> nxt[110];
int size[110];
char L[110];
char WB[110];

void dfs(int u){
	size[u] = 1;
	for(int v : nxt[u]){
		dfs(v);
		size[u] += size[v];
	}
}

vector<string> ways;
mt19937_64 eng;

void generate(int r, int n){
	ways[r].clear();
	vector<int> cur = nxt[0];
	FWD(i,0,n){
		int c = uniform_int_distribution<int>(0, n-i-1)(eng);
		int p = 0;
		int t = 0;
		for(;;){
			t += size[cur[p]];
			if(t > c) break;
			++p;
		}
		swap(cur[p], cur.back());
		int u = cur.back();
		cur.pop_back();
		ways[r].push_back(L[u]);
		cur.insert(cur.end(), nxt[u].begin(), nxt[u].end());
	}
}

bool issubstr(string a, string b){
	FWD(i,0,SIZE(a)-SIZE(b)+1){
		bool ok = 1;
		FWD(j,0,SIZE(b)){
			if(a[i+j] != b[j]){
				ok = 0;
				break;
			}
		}
		if(ok) return 1;
	}
	return 0;
}


int TRIES = 50000;

void solve() {
	int n;
	scanf("%d", &n);
	FWD(i,0,n+1) nxt[i].clear();
	FWD(i,1,n+1){
		int p;
		scanf("%d", &p);
		nxt[p].push_back(i);
	}
	dfs(0);
	ways.resize(TRIES);
	scanf("%s", L+1);
	FWD(r,0,TRIES) generate(r, n);
	int m;
	scanf("%d", &m);
	FWD(i,0,m){
		scanf("%s", WB);
		string W(WB);
		int t = 0;
		FWD(r,0,TRIES){
			if(issubstr(ways[r], WB)) ++t;
		}
		printf("%.3Lf ", (long double)t/TRIES);
	}
	printf("\n");
}

int main(){
	int zzz;
	scanf("%d", &zzz);
	FWD(zz,1,zzz+1){
		printf("Case #%d: ", zz);
		solve();
	}
	return 0;
}
