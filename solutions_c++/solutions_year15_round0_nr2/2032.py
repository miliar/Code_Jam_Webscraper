#include <cstdio>
#include <algorithm>
#include <vector>

#define FOR(a,b,c) for (int c = (a), _for = (b); c < _for; ++c)
#define REP(n) for (int _rep = 0, _for = (n); _rep < _for; ++_rep)
#define pb push_back
#define x first
#define y second
#define ll long long

using namespace std;

const int oo = 1000000000;

int D;
int P[1005];

int Count(int Limit){
	int R = Limit;
	FOR(0, D, i) R += (P[i] - 1) / Limit;
	return R;
}

int Solve(){
	scanf("%d", &D);
	FOR(0, D, i) scanf("%d", P + i);
	
	int R = oo;
	FOR(1, 1001, i) R = min(R, Count(i));
	return R;
	
}

int main(){
	int t;
	scanf("%d", &t);
	FOR(1, t + 1, i){
		printf("Case #%d: %d\n", i, Solve());
	}
	return 0;
}
