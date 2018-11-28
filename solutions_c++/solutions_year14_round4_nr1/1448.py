/*
 * pa.cpp
 * Copyright (C) 2014 KuoE0 <kuoe0.tw@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

int main() {

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {

		deque<int> item;
		int n, m;
		cin >> n >> m;

		for (int i = 0; i < n; ++i) {
			int x;
			cin >> x;
			item.push_back(x);
		}

		sort(item.begin(), item.end());


		int cnt = 0;

		while (!item.empty()) {
			++cnt;

			int total = item.back();
			item.pop_back();

			if (!item.empty() && total + item.front() <= m) {
				item.pop_front();
			}
		}

		cout << "Case #" << t + 1 << ": " << cnt << endl;

	}

	return 0;
}




