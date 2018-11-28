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
#define N 30

int n;
char s[N][N];

int used[N];
bool check(int *perm, int cur)
{
	if (cur == n)return true;

	bool found = false;
	for (int i = 0; i < n; ++i)if (s[perm[cur]][i] == '1')
	{
		if (used[i]) continue;
		if (!used[i]) found = true;
		used[i] = true;
		if (!check(perm, cur + 1))
		{
			used[i] = false;
			return false;
		}
		used[i] = false;
	}
	return found;
}

int main()
{
	ifstream cin("D-small-attempt2.in");
	ofstream cout("C.out");

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cin >> n;
		for (int i = 0; i < n; ++i)cin >> s[i];

		int pw = 1 << (n*n);
		int ans = n*n;
		for (int state = 0; state < pw; ++state)
		{
			bool need = true;
			int sum = 0;
			for (int cur = state, num = 0; cur > 0; cur /= 2, num += 1)
			{
				if (cur & 1)
				{
					int n1 = num / n;
					int n2 = num % n;
					if (s[n1][n2] == '1')
					{
						need = false;
						break;
					}
					sum += 1;
				}
			}
			if (!need || sum > ans)
			{
				continue;
			}

			for (int cur = state, num = 0; cur > 0; cur /= 2, num += 1)
			{
				if (cur & 1)
				{
					int n1 = num / n;
					int n2 = num % n;
					s[n1][n2] = '1';
				}
			}

			int perm[N];
			bool bOk = true;
			for (int i = 0; i < n; ++i)perm[i] = i;
			do
			{
				memset(used, 0, sizeof(used));
				if (!check(perm, 0))
				{
					bOk = false;
					break;
				}
			} while (std::next_permutation(perm, perm + n));

			if (bOk)
			{
				ans = min(ans, sum);
			}
			
			for (int cur = state, num = 0; cur > 0; cur /= 2, num += 1)
			{
				if (cur & 1)
				{
					int n1 = num / n;
					int n2 = num % n;
					s[n1][n2] = '0';
				}
			}
		}
		cout << "Case #" << t + 1 << ": "<<ans<<endl;
	}
	re 0;
}