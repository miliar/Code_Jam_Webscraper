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

bool good(bool ar[])
{
	for (int i = 0; i < 10; ++i)
		if (!ar[i])
			return false;
	return true;
}

void get(bool ar[], ui c)
{
	while (c > 0)
	{
		ar[c % 10] = true;
		c = c / 10;
	}
}

int main()
{
	cin.sync_with_stdio(false);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	ll n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		ui x;
		cin >> x;
		cout << "Case #" << i+1 << ": ";
		if (x == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		bool used[10] = {};
		ui nx = x;
		while (true)
		{
			get(used, nx);
			if (good(used))
			{
				cout << nx << endl;
				break;
			}
			else
				nx += x;
		}
	}
	return 0;
}