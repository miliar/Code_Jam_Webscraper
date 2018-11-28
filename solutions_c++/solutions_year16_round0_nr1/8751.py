#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>

using namespace std;

set<long long> q;

void f(long long ans)
{
	while (ans != 0)
	{
		long long v = ans % 10;
		q.insert(v);
		ans /= 10;
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
/*
	cout << 1000001 << endl;
	for (long long i = 0; i < 1000001; i++)
		cout << i << endl;
	return 0;*/
	long long t;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		long long n;
		cin >> n;
		q.clear();
		cout << "Case #" << i + 1 << ": ";
		if (n == 0)
		{
			cout << "INSOMNIA\n";
			continue;
		}
		long long ans = 0;
		while (q.size() != 10)
		{
			ans += (long long)n;
			f(ans);
		}
		cout << ans << endl;

	}



	return 0;
}