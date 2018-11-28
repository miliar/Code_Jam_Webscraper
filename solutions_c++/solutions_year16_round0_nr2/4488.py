#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

#define M_PI 3.14159265358979323846

using namespace std;

typedef unsigned __int64 ui;
typedef __int64 si;
typedef long long ll;

bool good(string ar)
{
	for (int i = 0; i < ar.length(); ++i)
		if (ar[i] == '-')
			return false;
	return true;
}

int main()
{
	cin.sync_with_stdio(false);
	freopen("B-large.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	ll n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		string a;
		cin >> a;
		int m = 0;
		while (true)
		{
			for (int i = a.length() - 1; i >= 0; --i)
			{
				if (a[i] == '-')
				{
					for (int j = 0; j <= i; ++j)
					{
						if (a[j] == '-')
							a[j] = '+';
						else
							a[j] = '-';
					}
					++m;
					break;
				}
			}
			if (good(a))
				break;
		}
		cout << "Case #" << i+1 << ": " << m << endl;
	}
	return 0;
}