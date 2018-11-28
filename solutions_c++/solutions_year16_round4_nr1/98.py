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

map<tuple<char, int, int, int>, string> pos[13];

void solve(){
	int n, r, p, s;
	scanf("%d %d %d %d", &n, &r, &p, &s);
	string res = "Z";
	tuple<char, int, int, int> ng;

	ng = make_tuple('R', r, p, s);
	if(pos[n].find(ng) != pos[n].end())
		res = min(res, pos[n][ng]);

	ng = make_tuple('P', r, p, s);
	if(pos[n].find(ng) != pos[n].end())
		res = min(res, pos[n][ng]);

	ng = make_tuple('S', r, p, s);
	if(pos[n].find(ng) != pos[n].end())
		res = min(res, pos[n][ng]);

	if(res == "Z")
		printf("IMPOSSIBLE\n");
	else
		printf("%s\n", res.c_str());
}

char res[256][256];

int main(){
	res['R']['R'] = 0;
	res['R']['P'] = 'P';
	res['R']['S'] = 'R';
	res['P']['R'] = 'P';
	res['P']['P'] = 0;
	res['P']['S'] = 'S';
	res['S']['R'] = 'R';
	res['S']['P'] = 'S';
	res['S']['S'] = 0;

	pos[0][make_tuple('R', 1, 0, 0)] = "R";
	pos[0][make_tuple('P', 0, 1, 0)] = "P";
	pos[0][make_tuple('S', 0, 0, 1)] = "S";
	char w0, w1;
	int r0, r1, p0, p1, s0, s1;
	FWD(n,0,12){
		for(auto kv0 : pos[n]){
			tie(w0, r0, p0, s0) = kv0.first;
			for(auto kv1 : pos[n]){
				tie(w1, r1, p1, s1) = kv1.first;
				if(res[w0][w1] == 0) continue;
				string cur = "Z";
				tuple<char, int, int, int> ng = make_tuple(res[w0][w1], r0+r1, p0+p1, s0+s1);
				if(pos[n+1].find(ng) != pos[n+1].end())
					cur = pos[n+1][ng];
				pos[n+1][ng] = min(cur, kv0.second+kv1.second);
			}
		}
	}
	int zzz;
	scanf("%d", &zzz);
	FWD(zz,1,zzz+1){
		printf("Case #%d: ", zz);
		solve();
	}
	return 0;
}
