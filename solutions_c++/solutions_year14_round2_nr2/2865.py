#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <functional>

using namespace std;

#define REP(v, repeat) for(int v=0; v<(repeat); ++v)
#define REPD(v, repeat) for(int v=(repeat)-1; v>=0; --v)
#define FOR(v, start, end) for(int v=(start); v<=(end); ++v)
#define FORD(v, start, end) for(int v=(start); v>=(end); --v)
#define ROUNDING(x, dig) (floor((x) * pow(10, dig) + 0.5f) / pow(10, dig))
#define INF 99999999

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <string> VS;
typedef long long ll;
typedef unsigned long long ull;

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	//freopen("output.txt","w+", stdout);
#endif

	int t;
	int A, B, K;
	scanf("%d", &t);
	FOR(tc, 1, t)
	{
		int cnt = 0;
		scanf("%d%d%d", &A, &B, &K);
		FOR(a, 0, A - 1) FOR(b, 0, B - 1) if ((a&b) < K) ++cnt;
		printf("Case #%d: %d\n", tc, cnt);
	}
	return 0;
}