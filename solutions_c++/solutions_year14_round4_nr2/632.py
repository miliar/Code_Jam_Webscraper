#include <iostream>
#include <cstring>
#include <climits>
using namespace std;

const char lend = '\n';

const int N = 1001;

int vet[N], n;

int solve()
{
	int res = 0;
	for (int i = 0; i < n; ++i)
	{
		int a = 0, b = 0;
		for (int j = 0; j < i; ++j)
			a += vet[j] > vet[i];
		for (int j = i+1; j < n; ++j)
			b += vet[j] > vet[i];
		res += min(a, b);
	}
	return res;
}

int main() 
{
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	
	for (int caso = 1; caso <= t; ++caso)
	{
		cout << "Case #" << caso << ": ";
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> vet[i];
		int res = solve();
		cout << res << lend;
	}
}
