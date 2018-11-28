#include <iostream>
#include <algorithm>
using namespace std;

const char lend = '\n';

const int N = 10000;

int n, d, vet[N];

int solve(int b)
{
	int r = b, j = n-b-1;
	for (int i = 0; i <= j; ++i, --j)
	{
		if (i != j && vet[i]+vet[j] > d) return N;
		++r;
	}
	return r;
}

int main() 
{
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	
	for (int caso = 1; caso <= t; ++caso)
	{
		cout << "Case #" << caso << ": ";
		cin >> n >> d;
		for (int i = 0; i < n; ++i)
			cin >> vet[i];
		sort(vet, vet+n);
		int res = N;
		for (int i = 0; i < n; ++i)
			res = min(res, solve(i));
		cout << res << lend;
	}
}
