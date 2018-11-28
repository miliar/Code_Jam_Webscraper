
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
const int MAXN = 101;
const int MAXH = 201;
const int MAXHIT = 1001;
int H[MAXN], G[MAXN];
int F[MAXN][MAXH][MAXHIT];
int P, Q, N;
void update(int &r, int d) { r = max(d, r); }
int main(){
	int tt;
	int  p, q, r, s;
	scanf("%d", &tt);
	for (int tcas = 1; tcas <= tt; tcas++){
		scanf("%d%d%d", &P, &Q, &N);
		for (int i = 0; i < N; i++) scanf("%d%d", &H[i], &G[i]);
		for (int i = 0; i <= N; ++i) memset(F[i], -1, sizeof(F[i]));
		F[0][H[0]][1] = 0;
		for (int i = 0; i < N; ++i)
			for (int j = H[i]; j >= 0; --j)
				for (int k = 0; k < MAXHIT; ++k) if (F[i][j][k] >= 0)
				{
					update(j <= Q ? F[i + 1][H[i + 1]][k + 1] : F[i][j - Q][k + 1], F[i][j][k]);
					if (k > 0)
					{
						int d = (j - 1) / P + 1;
						if (d <= k) update(F[i + 1][H[i + 1]][k - d], F[i][j][k] + G[i]);
					}
				}
		int ans = 0;
		for (int k = 0; k < MAXHIT; ++k) update(ans, F[N][H[N]][k]);
		printf("Case #%d: %d\n", tcas, ans);
	}
}
