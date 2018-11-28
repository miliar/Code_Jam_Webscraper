#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <cstdio>

using namespace std;

pair <int, int> solve()
{
	int n;
	cin >> n;
	deque <double> Ken(n);
	deque <double>	Naomi(n);

	for (int i = 0; i < n; ++i)
		cin >> Naomi[i];
	sort(Naomi.begin(), Naomi.end());

	for (int i = 0; i < n; ++i)
		cin >> Ken[i];
	sort(Ken.begin(), Ken.end());
	int decieve = 0;

	for (int i = 0; i < n; ++i)
	{
		if (Ken[i] < Naomi[i])
			++decieve;
		else
		{
			swap(Ken[i], Ken[Ken.size() - 1]);
			sort(Ken.begin() + i + 1, Ken.end());
		}
	}

	sort(Ken.begin(), Ken.end());

	int war = 0;
	while (!Naomi.empty())
	{
		double Naomi_turn = Naomi.back();
		Naomi.pop_back();
		if (Ken[Ken.size() - 1] < Naomi_turn)
		{
			++war;
			Ken.pop_front();
		}
		else
		{
			int pos = Ken.size() - 1;
			while (pos >= 0 && Ken[pos] > Naomi_turn)
				--pos;
			Ken.erase(Ken.begin() + pos + 1);
		}
	}
	return make_pair(decieve, war);
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		pair <int, int> ans = solve();
		cout << "Case #" << i << ": " << ans.first << ' ' << ans.second << endl;
	}
}