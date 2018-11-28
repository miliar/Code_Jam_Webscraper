#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
#define re return
#define LL unsigned long long
#define EPS 0.00000000000001
#define MOD 1000000009
#define INF 1000000000000000000LL
#define N 501

int n, k;
double p[N];

double prob[2][2 * N];

int main()
{
#ifdef _DINARISIO
	ifstream cin("B-small-attempt2.in");
	ofstream cout("B.out");
#endif

	int T;
	cin >> T;
	cout.precision(60);

	for (int t = 0; t < T; ++t)
	{
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
		{
			cin >> p[i];
		}

		int len = 1 << n;
		double ans = 0;
		for (int state = 0; state < len; ++state)
		{
			int actives = 0;
			for (int cur = state; cur > 0; cur /= 2)actives += cur & 1;
			if (actives != k) continue;
			
			int odd = 0;
			actives = 0;
			/*for (int sum = -actives - 1; sum <= actives + 1; ++sum)
			{
				prob[odd][N + sum] = 0;
			}*/
			memset(prob[odd], 0, sizeof(prob[odd]));
			prob[odd][N + 0] = 1;
			for (int cur = state, num = 0; cur > 0; cur /= 2, ++num)
			{
				if (cur & 1)
				{
					int nextOdd = odd ^ 1;
					for (int sum = -actives - 1; sum <= actives + 1; ++sum)
					{
						prob[nextOdd][N + sum + 1] += prob[odd][N + sum] * p[num];
						prob[nextOdd][N + sum - 1] += prob[odd][N + sum] * (1 - p[num]);
						//prob[odd][N + sum] = 0;
					}
					memset(prob[odd], 0, sizeof(prob[odd]));
					odd = nextOdd;
					actives += 1;
				}
			}
			ans = max(ans, prob[odd][N + 0]);
		}

		cout << "Case #" << t + 1 << ":";
		cout << fixed << " " << ans << endl;
	}
	re 0;
}