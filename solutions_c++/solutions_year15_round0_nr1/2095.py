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

int Smax;
char in[1005];

int Solve(){
	scanf("%d%s", &Smax, in);
	int Cnt = 0;
	int R = 0;
	FOR(0, Smax + 1, i){
		if (Cnt < i) R += i - Cnt, Cnt = i;
		Cnt += in[i] - '0';
	}
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

