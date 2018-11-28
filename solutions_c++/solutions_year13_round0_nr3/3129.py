#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

bool isp(int x)
{
	int a[10], l = 0;
	while (x)
		a[l++] = x % 10, x /= 10;
	for (int i = 0, j = l - 1; i <= j; i++, j--)
		if (a[i] != a[j])
			return 0;
	return 1;
}

bool is(int x)
{
	if (!isp(x))	return 0;
	int s = sqrt(double(x));
	if (s * s == x && isp(s))	return 1;
	return 0;
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;		cin >> tc;
	for (int T = 1; T <= tc; T++)
	{
		int a, b;	cin >> a >> b;
		int num = 0;
		for (int i = a; i <= b; i++)
			if (is(i))
				num++;
		cout<< "Case #" << T << ": " << num << endl;
	}
}