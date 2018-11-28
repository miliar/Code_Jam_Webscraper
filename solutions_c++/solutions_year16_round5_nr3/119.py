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

struct p3 {
    K x, y, z;
    p3(K xi, K yi, K zi):x(xi), y(yi), z(zi) {}
    p3() {}
    K norm() const { return x*x+y*y+z*z; } // kwadrat(!)
};

p3 operator+(p3 a, p3 b) { return p3(a.x+b.x, a.y+b.y, a.z+b.z); }
p3 operator-(p3 a, p3 b) { return p3(a.x-b.x, a.y-b.y, a.z-b.z); }
p3 operator*(p3 a, K f) { return p3(a.x*f, a.y*f, a.z*f); }

K dist_limit, stay_limit, time_limit = 30000;

p3 vel[1010];
p3 pos[1010];
K midd[1010][1010];

K dist(int u, int v, K t){
	return sqrt((pos[u]+vel[u]*t-pos[v]-vel[v]*t).norm());
}

void calculate_clo(int u, int v){
	K lo = 0;
	K hi = time_limit;
	FWD(r,0,60){
		K mi0 = (2*lo + hi) / 3;
		K mi1 = (lo + 2*hi) / 3;
		if(dist(u, v, mi0) < dist(u, v, mi1)){
			hi = mi1;
		}else{
			lo = mi0;
		}
	}
	midd[u][v] = lo;
}

bool calculate_jump_interval(int u, int v, K &from, K &to){
	K clo = midd[u][v];
	if(dist(u, v, clo) > dist_limit){
		return 0;
	}
	from = 0;
	to = time_limit;
	return 1;
	K lo, hi;
	lo = 0;
	hi = clo;
	FWD(r,0,30){
		K mi = (lo + hi) / 2;
		if(dist(u,v,mi) < dist_limit){
			hi = mi;
		}else{
			lo = mi;
		}
	}
	from = hi;
	lo = clo;
	hi = time_limit;
	FWD(r,0,30){
		K mi = (lo + hi) / 2;
		if(dist(u,v,mi) < dist_limit){
			lo = mi;
		}else{
			hi = mi;
		}
	}
	to = lo;
	/*printf("jump %d - %d\n", u, v);
	printf("	%Lf\n", dist(u, v, clo));
	printf("	%Lf %Lf\n", from, dist(u, v, from));
	printf("	%Lf %Lf\n", to, dist(u, v, to));*/
	return 1;
}

struct event {
	K time;
	int type;
	/*
	0 - edge appear
	1 - edge dissapear
	2 - cannot stay on astro
	*/
	int u, v;
};

bool operator<(event a, event b){
	return a.time > b.time;
}

int n;
set<int> out[1010];
K stay[1010];
bool reach[1010];
int vis[1010];
vector<int> comp;
int stamp;

void dfs(int u){
	vis[u] = stamp;
	comp.push_back(u);
	for(int v : out[u]) if(vis[v] < stamp) dfs(v);
}

const K EPS = 1e-6;

bool verify(){
	FWD(i,0,n) vis[i] = 0;
	stamp = 0;
	priority_queue<event> Q;
	FWD(i,0,n){
		out[i].clear();
		FWD(j,i+1,n){
			K from, to;
			if(calculate_jump_interval(i, j, from, to)){
				Q.push(event{from, 0, i, j});
				Q.push(event{to, 1, i, j});
			}
		}
	}
	FWD(i,0,n) reach[i] = 0;
	reach[0] = 1;
	stay[0] = stay_limit;
	Q.push(event{stay_limit, 2, 0, -1});
	while(!Q.empty()){
		event e = Q.top();
		Q.pop();
		int u = e.u;
		int v = e.v;
		if(e.type == 2){
			if(!(stay[u]-e.time > EPS)){
				reach[u] = 0;
			}
		}else{
			if(e.type == 0){
				stay[u] = stay[v] = time_limit;
				if(reach[u] && !reach[v]){
					++stamp;
					comp.clear();
					dfs(v);
					for(int x : comp) reach[x] = 1;
				}
				if(reach[v] && !reach[u]){
					++stamp;
					comp.clear();
					dfs(u);
					for(int x : comp) reach[x] = 1;
				}
				out[u].insert(v);
				out[v].insert(u);
			}else{
				out[u].erase(v);
				out[v].erase(u);

				if(SIZE(out[u]) == 1){
					if(stay[u] - e.time - stay_limit > EPS){
						stay[u] = e.time + stay_limit;
						Q.push(event{e.time + stay_limit, 2, u, -1});
					}
				}

				if(SIZE(out[v]) == 1){
					if(stay[v] - e.time - stay_limit > EPS){
						stay[v] = e.time + stay_limit;
						Q.push(event{e.time + stay_limit, 2, v, -1});
					}
				}
			}
		}
		if(reach[1]){
			return 1;
		}
	}
	return 0;
}

void solve(){
	scanf("%d", &n);
	scanf("%Lf", &stay_limit);
	FWD(i,0,n){
		scanf("%Lf %Lf %Lf", &pos[i].x, &pos[i].y, &pos[i].z);
		scanf("%Lf %Lf %Lf", &vel[i].x, &vel[i].y, &vel[i].z);
	}
	FWD(i,0,n) FWD(j,i+1,n) calculate_clo(i, j);
	/*FWD(i,0,n){
		FWD(j,i+1,n){
			printf("%d -- %d %Lf\n", i, j, dist(i, j, 0));
		}
	}*/
	
	K lo = 0;
	K hi = 3000;
	FWD(r,0,27){
		dist_limit = (lo + hi) / 2;
		if(verify()){
			hi = dist_limit;
		}else{
			lo = dist_limit;
		}
	}
	printf("%.7Lf\n", hi);
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
