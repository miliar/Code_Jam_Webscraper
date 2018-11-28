#pragma warning (disable : 4996)

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <functional>
#include <iomanip>
#include <queue>




using namespace std;


#define forn(i, n) for(int i = 0; i < n; ++i)
#define down(i, n) for(int i = n - 1; i >= 0; --i)



typedef long long int i64;
typedef vector<i64> vint;

bool isHappy(int a)
{
	do
	{
		int b = a % 10;
		if (b != 4 && b != 7)
			return false;
		a /= 10;
	} while (a > 0);
	return true;
}

bool check(vector<string> & arr, int x, int y)
{
	int s = 0;
	forn(i, 2)
	{
		forn(j, 2)
		{
			if (arr[x + i][y + j] == '.')
			{
				s++;
			}
		}
	}
	return s != 2;
}

int main()
{

	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(10);
#ifdef FILE_INPUT
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

#endif
	int T;
	cin >> T;
	forn(t, T)
	{
		int n, x;
		cin >> n >> x;
		vint arr(n);
		forn(i, n)
		{
			cin >> arr[i];
		}
		sort(arr.begin(), arr.end(), greater<int>());
		int ans = 0;
		vint used(n);
		int r = n - 1;
		forn(i, n)
		{
			if (!used[i])
			{
				used[i] = 1;
				int w = arr[i];
				if (r != i)
				{
					if (arr[r] + w <= x)
					{
						used[r] = 1;
						--r;
					}
				}
				++ans;

			}
		}


		cout << "Case #" << t + 1 << ": ";
		cout << ans;
		cout << "\n";
	}
	return 0;
}