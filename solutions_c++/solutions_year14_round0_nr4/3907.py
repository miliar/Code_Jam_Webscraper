#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

bool ken_step(double a, set<double> &b)
{
	auto it = b.lower_bound(a);
	if(it == b.end())
	{
		b.erase(b.begin());
		return false;
	}
	else
	{
		b.erase(it);
		return true;
	}
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		double x;
		cin >> n;
		vector<double> va, vb;
		set<double> a, b;
		for (int j = 0; j < n; ++j) cin >> x, a.insert(x), va.push_back(x);
		for (int j = 0; j < n; ++j) cin >> x, b.insert(x), vb.push_back(x);
		sort(va.begin(), va.end());
		sort(vb.begin(), vb.end());
		int answer1 = 0, answer2 = 0;
		for (int j = n-1; j>=0; --j)
			if(ken_step(va[j], b) == false) answer2++;
		for (int j = n-1; j>=0; --j)
			if(ken_step(vb[j], a) == true) answer1++;
		printf("Case #%d: %d %d\n", i, answer1, answer2);
	}
}