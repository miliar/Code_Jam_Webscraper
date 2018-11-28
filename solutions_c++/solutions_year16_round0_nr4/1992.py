#include <iostream>
using namespace std;

int nowtd, tdnum;

long long i, j, k, c, s;

long long geti(long long st, long long k, long long c)
{
	int j;

	long long result = 0;

	for (j = 0; j < c; j++)
	{
		if (st >= k) st = k - 1;
		result = result * k + st++;
	}
	cout << result + 1 << " ";
	return st;
}

int main()
{
	cin >> tdnum;
	for (nowtd = 1; nowtd <= tdnum; nowtd++)
	{
		cin >> k >> c >> s;
		cout << "Case #" << nowtd << ": ";
		if (s * c >= k)
			for (i = 0; i < k; i = geti(i, k, c));
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
