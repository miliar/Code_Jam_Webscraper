#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(vector<double>& a, vector<double>& b) // a is "winning"
{
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	int n = (int)a.size();

	int r = 0;
	int i = n-1;
	for(int j = n-1; j >= 0; --j)
		if(a[i] > b[j])
		{
			++r;
			i--;
		}
	return r;
}

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		vector<double> a, b;
		int n;

		cin >> n;
		a.resize(n);
		b.resize(n);

		for(int i = 0; i < n; ++i)
			cin >> a[i];
		for(int i = 0; i < n; ++i)
			cin >> b[i];

		cout << "Case #" << t << ": " << solve(a, b) << " " << n-solve(b, a) << endl;
	}
}
