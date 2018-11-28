#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

int mr = 1e9;

void solve(int sm, vector<int> d, int p)
{
	int curT = 0;
	int mx = 0, pos;
	for (int i = 0; i < d.size(); ++i)
	{
		if (mx < d[i])
		{
			mx = d[i];
			pos = i;
		}
	}
	

	mr = min(mr, mx + p);

	if (mx <= 2) return;

	if (d[pos] % 2 == 0)
	{
		vector<int> tmp = d;
		tmp.push_back(tmp[pos] / 2);
		tmp[pos] /= 2;
		solve(sm, tmp, p + 1);
	}
	if (d[pos] % 2 != 0)
	{
		vector<int> tmp = d;
		tmp.push_back((tmp[pos] / 2) + 1);
		tmp[pos] /= 2;
		solve(sm, tmp, p + 1);
	}
	if (mx == 9)
	{
		vector<int> tmp = d;
		tmp.push_back(3);
		tmp[pos] = 6;
		solve(sm, tmp, p + 1);
	}

}


int main()
{
freopen("C:\\out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		
		int n;
		cin >> n;
		vector <int> d(n);
		mr = 1e9;
		for (int i = 0; i < n; ++i)
			cin >> d[i];
		sort(d.begin(), d.end());
		solve(n, d, 0);
		cout << "Case #" << i + 1 << ": ";
		cout << mr << endl;
	}
}