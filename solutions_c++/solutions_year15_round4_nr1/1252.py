// #include C/C++ {
#include <bits/stdc++.h>
// }
using namespace std;
// #typedef {
typedef long long int64;
typedef unsigned long long uint64;
typedef pair <int, int> PII;
typedef pair <char, char> PCC;
typedef pair <int64, int64> PLL;
typedef pair <double, double> PDD;
// }

// #parameter{
#ifdef DEBUG_MODE

#define TYPE decltype
#define RF(filename) {freopen((filename), "r", stdin);}
#define WF(filename) {freopen((filename), "w", stdout);}
#define DEBUG printf

#else

#define TYPE __typeof
#define RF(filename) {;}
#define WF(filename) {;}
#define DEBUG(...)

#endif

// #define {
#define SZ(a) ((int)(a).size())
#define X first
#define Y second
#define MP make_pair
#define L(x) ((x)<<1)
#define R(x) ((x)<<1 | 1)
#define max3(x, y, z) (max(max((x), (y)), (z)))
#define min3(x, y, z) (min(min((x), (y)), (z)))
#define BIT(x, i) (((x) >> (i)) & 1)
#define ALL(it) (it).begin(), (it).end()
#define FILL(__space, __val) memset(__space, __val, sizeof(__space))
#define MOVE(__spaceTo, __spaceFrom) memmove(__spaceTo, __spaceFrom, sizeof(__spaceTo))
#define FOR(it, c) for( TYPE((c).begin()) it = (c).begin(); it != (c).end(); it++)
/////////////////////////////////////////////////////////////
const double PI = acos(-1.0);
const double EPS = 1e-6;

#define MAX_N 205
#define MAX_M 22
#define MAXX 0x3f
#define UPPER 2147483647LL
#define INF ((1 << 30) - 1)
#define BINF ((1LL << 62) - 1LL)
#define NONE -1
#define NIL 0
// }

/////////////////////////////////////////////////////////////
char mapp[MAX_N][MAX_N];
char tmp[MAX_N][MAX_N];
int change[MAX_N][MAX_N];
void Init(){
	FILL(change, 0);
}
int R, C;
void Update(){
	MOVE(tmp, mapp);
	//up to down
	for (int c = 0; c < C; c++) for (int r = 0; r < R; r++) if (mapp[r][c] != '.'){
		if (tmp[r][c] == '^'){
			tmp[r][c] = '<';
			change[r][c]++;
		}
		break;
	}
	//left to right
	for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) if (mapp[r][c] != '.'){
		if (tmp[r][c] == '<'){
			tmp[r][c] = 'v';
			change[r][c]++;
		}
		break;
	}
	//down to up
	for (int c = 0; c < C; c++) for (int r = R - 1; r >= 0; r--) if (mapp[r][c] != '.'){
		if (tmp[r][c] == 'v'){
			tmp[r][c] = '>';
			change[r][c]++;
		}
		break;
	}
	//right to left
	for (int r = 0; r < R; r++) for (int c = C - 1; c >= 0; c--) if (mapp[r][c] != '.'){
		if (tmp[r][c] == '>'){
			tmp[r][c] = '^';
			change[r][c]++;
		}
		break;
	}
	MOVE(mapp, tmp);
}
int Solve(){
	int res = 0;
	for (int r = 0; r < R; r++) for (int c = 0; c < C; c++){
		if (change[r][c] >= 4)
			return NONE;
		if (change[r][c] > 0)
			res++;
	}
	return res;
}
/////////////////////////////////////////////////////////////
int main(){
	RF("input.txt");
	WF("output.txt");

	int T;
	scanf("%d", &T);
	for (int _ = 1; _ <= T; _++){
		Init();
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; r++) scanf("%s", mapp[r]);
		Update();
		Update();
		Update();
		Update();
		int res = Solve();
		printf("Case #%d: ", _);
		if (res == NONE)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", res);
	}
	return 0;
}
