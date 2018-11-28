#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

double a[200], b[200];

int calc(int n, double* a, double* b)
{
	int ret = 0;
	int ptr = 0;
	for(int i = 0; i < n; ++i)
	{
		while(ptr < n && a[ptr] < b[i])
			++ptr;
		if(ptr < n)
		{
			++ptr;
			++ret;
		}
	}
	return ret;
}

int main()
{
	freopen("inputD.txt", "r", stdin);
	freopen("outputD.txt", "w", stdout);
	int Count;
	cin >> Count;
	for(int T = 1; T <= Count; ++T)
	{
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i)
			cin >> a[i];
		for(int i = 0; i < n; ++i)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		printf("Case #%d: %d %d\n", T, calc(n, a, b), n - calc(n, b, a));
	}
}
