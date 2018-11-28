// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <set>
#include <algorithm>
#include <cassert>
#include <vector>
#include "ConsoleApplication1.h"

using namespace std;

constexpr int MAXP = 1000;

int cut[MAXP + 1][MAXP + 1];

auto dp()
{
	for (auto k = 1; k <= MAXP; ++k)
		for (auto i = 1; i <= MAXP; ++i) {
			auto res = MAXP;
			if (i <= k) res = 0;
			for (auto j = 1; j <= i - 1; ++j)
				res = min(res, 1 + cut[k][j] + cut[k][i - j]);
			cut[k][i] = res;
		}
}

auto solve2()
{
	int d; cin >> d;
	auto v = vector<int>(d);
	for (auto& x : v) cin >> x;
	auto big = *std::max_element(v.begin(), v.end());
	auto res = big;
	for (auto k = 1; k <= big; ++k) {
		auto cur = 0;
		for (auto x : v)
			cur += cut[k][x];
		cur += k;
		res = min(res, cur);
	}
	return res;
}

auto solve()
{
	int d; cin >> d;
	auto s = multiset<int>();
	for (auto i = 0; i < d; ++i) {
		int x; cin >> x;
		s.insert(x);
	}
	auto res = *(s.rbegin());
	auto steps = 0;
	while (!s.empty()) {
		auto big = *(s.rbegin());
		s.erase(--s.end());
		res = min(res, big + steps);
		if (big == 1) break;
		assert(big / 2 > 0);
		s.insert((big + 1) / 2);
		s.insert(big / 2);
		++steps;
		if (steps > res) break;
	}
	return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	dp();
	int t; cin >> t;
	for (int q = 0; q < t; ++q)
		cout << "Case #" << (q + 1) << ": " << solve2() << endl;
	return 0;
}

