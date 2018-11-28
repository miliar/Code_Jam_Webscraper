/*
ID: alperca1
LANG: C++
TASK: dualpal
*/

#include <bits/stdc++.h>

#ifdef NOT_UVA
#include <Windows.h>
#endif

using namespace std;

typedef unsigned long long ull;
typedef pair<ull, int> ulli;
typedef pair<int, int> ii;

#define INF (1<<30)

double pi = 3.14;

int count(int n)
{
	int seen[10] = { 0 };

	if (n == 0) return -1;
	int i = 1;
	while (true)
	{
		int cpy = n*i;

		do
		{
			seen[cpy % 10]++;
			cpy /= 10;
		} while (cpy);

		bool all = true;
		for (int i = 0; i < 10; ++i)
		{
			if (!seen[i])
			{
				all = false;
				break;
			}
		}

		if (all) return i*n;
		else ++i;
	}
}

int main(int argc, char **argv)
{
	//ios_base::sync_with_stdio(false);
#ifndef NOT_UVA
	//freopen("daireler.gir", "r", stdin);
	freopen("daireler.cik", "w", stdout);
#endif
	freopen("daireler.cik", "w", stdout);
	int t;

	cin >> t;
	int cnt = 1;
	while (t--)
	{
	
		int n;
		cin >> n;
		cout << "Case #" << cnt++ << ": ";
		int res = count(n);
		if (res == -1) cout << "INSOMNIA";
		else cout << res;

			cout << endl;
	}

	end:
#ifdef NOT_UVA
	//Sleep(-1);
#endif

	return 0;
}

