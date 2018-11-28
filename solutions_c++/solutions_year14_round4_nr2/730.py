#pragma warning (disable : 4996)

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <functional>
#include <iomanip>
#include <cassert>
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

void check(vint & arr)
{
	if (arr.size())
	forn(i, arr.size() - 1)
	{
		assert(arr[i] < arr[i + 1]);
	}
}



int getAnsUp(int m, int p, vint & arr)
{
	int ans = 0;
	vint f;
	forn(i, m)
	{
		if (i != p)
		{
			f.push_back(arr[i]);
		}
		else
		{
			++m;
		}
	}
	forn(i, f.size())
	{
		forn(j, f.size() - 1)
		{
			if (f[j] > f[j + 1])
			{
				ans++;
				swap(f[j], f[j + 1]);
			}
		}
	}
	check(f);
	return ans;
}

int getAnsDown(int m, int p, vint & arr)
{
	int ans = 0;
	vint f;
	for (int i = arr.size() - 1; i > m; --i)
	{
		if (i != p)
		{
			f.push_back(arr[i]);
		}
		else
		{
			--m;
		}
	}
	forn(i, f.size())
	{
		forn(j, f.size() - 1)
		{
			if (f[j] > f[j + 1])
			{
				ans++;
				swap(f[j], f[j + 1]);
			}
		}
	}
	check(f);
	return ans;
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
		int n;
		cin >> n;
		vint arr(n);
		forn(i, n)
		{
			cin >> arr[i];
		}
		int maxim = -1000;
		int pos = 0;
		forn(i, n)
		{
			if (arr[i] > maxim)
			{
				maxim = arr[i];
				pos = i;
			}
		}
		int ans = 0;
		int res = n;
		forn(i, res)
		{
			int minim = *min_element(arr.begin(), arr.end());
			int pos;
			forn(j, n)
			{
				if (arr[j] == minim)
				{
					pos = j;
					ans += min(j, n - j - 1);
				}
			}
			vint cop(n - 1);
			int p = 0;
			forn(i, n - 1)
			{
				if (arr[p] != minim)
					cop[i] = arr[p];
				else
				{
					--i;
				}
				++p;
			}
			arr = cop;
			--n;


		}

		cout << "Case #" << t + 1 << ": ";
		cout << ans;
		cout << "\n";
	}
	return 0;
}