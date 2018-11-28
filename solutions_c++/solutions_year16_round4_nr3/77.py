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
typedef long double dd;
typedef vector<int> VI;

const int dx[] = {0,0,-1,1}; //1,1,-1,1};
const int dy[] = {-1,1,0,0}; //1,-1,1,-1};

int n, m;
int mate[303];
char res[17][17];

struct pos{
	int x, y, d;
};

//   0
//  3.1
//   2

pos nextpos(pos p){
	char c = res[p.x][p.y];
	if(c == '/'){
		if(p.d == 0){
			--p.y;
			p.d = 1;
		}else if(p.d == 1){
			++p.x;
			p.d = 0;
		}else if(p.d == 2){
			++p.y;
			p.d = 3;
		}else if(p.d == 3){
			--p.x;
			p.d = 2;
		}
	}else{
		if(p.d == 0){
			++p.y;
			p.d = 3;
		}else if(p.d == 1){
			--p.x;
			p.d = 2;
		}else if(p.d == 2){
			--p.y;
			p.d = 1;
		}else if(p.d == 3){
			++p.x;
			p.d = 0;
		}		
	}
	return p;
}

int getnumber(int x, int y){
	if(x == -1){
		return y+1;
	}
	if(x == n){
		return m+n+m-y;
	}
	if(y == -1){
		return m+n+m+n-x;
	}
	return m+1+x;
}

bool check(pos s, pos p){
	while(0 <= p.x && p.x < n && 0 <= p.y && p.y < m){
		p = nextpos(p);
	}
	return mate[getnumber(p.x, p.y)] == getnumber(s.x, s.y);
}

bool check(){
	FWD(i,0,n){
		if(!check(pos{i, -1, -1}, pos{i, 0, 3})) return 0;
		if(!check(pos{i, m, -1}, pos{i, m-1, 1})) return 0;
	}

	FWD(i,0,m){
		if(!check(pos{-1, i, -1}, pos{0, i, 0})) return 0;
		if(!check(pos{n, i, -1}, pos{n-1, i, 2})) return 0;
	}

	return 1;
}

bool solve(){
	scanf("%d %d", &n, &m);
	FWD(i,0,n+m){
		int a, b;
		scanf("%d %d", &a, &b);
		mate[a] = b;
		mate[b] = a;
	}
	FWD(mask,0,1<<(n*m)){
		FWD(i,0,n)
			FWD(j,0,m){
				if(mask&(1<<(i*m+j)))
					res[i][j] = '/';
				else
					res[i][j] = '\\';
			}
		if(check()){
			FWD(i,0,n){
				res[i][m] = 0;
				printf("%s\n", res[i]);
			}
			return 1;
		}
	}
	return 0;
}

int main(){
	int zzz;
	scanf("%d", &zzz);
	FWD(zz,1,zzz+1){
		printf("Case #%d:\n", zz);
		if(!solve())
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
