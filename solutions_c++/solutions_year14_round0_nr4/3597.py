#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(v, repeat) for(int v=0; v<(repeat); ++v)
#define REPD(v, repeat) for(int v=(repeat)-1; v>=0; --v)
#define FOR(v, start, end) for(int v=(start); v<=(end); ++v)
#define FORD(v, start, end) for(int v=(start); v>=(end); --v)
#define ROUNDING(x, dig) (floor((x) * pow(10, dig) + 0.5f) / pow(10, dig))
#define INF 99999999

typedef vector <double> VD;

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w+", stdout);
#endif

	int t;
	scanf("%d", &t);
	FOR(tc, 1, t)
	{
		int n, cnt1 = 0, cnt2 = 0;
		scanf("%d", &n);
		VD nao(n);
		VD ken(n);
		REP(i, n) scanf("%lf", &nao[i]);
		REP(i, n) scanf("%lf", &ken[i]);

		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());

		//game 1
		int idx = 0, back = n - 1;
		REP(i, n)
		{
			if (idx >= n || back < 0) break;
			if (nao.back() < ken[back])
			{
				--back;
				continue;
			}

			if (nao[i] < ken[idx])
				while (++i < n && nao[i] < ken[idx]) ;
			++idx;
			++cnt1;
		}

		// game2
		idx = 0;
		REP(i, n)
			if (nao[idx] < ken[i]) { idx++; cnt2++; }

		printf("Case #%d: %d %d\n", tc, cnt1, n-cnt2);
	}
	return 0;
}