#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

#define X first
#define Y second

typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;

const ull mod = 1000002013;

ull total_paid = 0;

// (Entry, Count)
priority_queue <pair <int, ull> > tickets;
int N;

void enter_subway(int at, ull count) {
	tickets.push(make_pair(at, count));
}

ull trip_cost(ull num, ull count) {
	ull n = N;
	ull single = (N + (N - num + 1)) * num / 2 % mod;

	return single * count % mod;
}

void submit_trip(ull num, ull count) {
	total_paid = (total_paid + trip_cost(num, count)) % mod;
}

void leave_subway(int at, ull count) {
	while (count > 0) {
		pair <int, ull> tmp = tickets.top();
		tickets.pop();

		submit_trip(at - tmp.first, min(count, tmp.second));

		if (tmp.second > count)
			tickets.push(make_pair(tmp.first, tmp.second - count));

		count -= min(count, tmp.second);
	}
}

int main() {
	int T;
	scanf("%d", &T);

	for (int TT = 1; TT <= T; ++TT) {
		total_paid = 0;
		int m;
		scanf("%d %d", &N, &m);
		vector <pair <int, int> > a;
		ull must_pay = 0;
		for (int i = 0; i < m; ++i) {
			int x, y, p;
			scanf("%d%d%d", &x, &y, &p);
			a.push_back(make_pair(x, -p));
			a.push_back(make_pair(y, p));
			must_pay = (must_pay + trip_cost(y - x, p)) % mod;
		}
		sort(a.begin(), a.end());

		for (int i = 0; i < a.size(); ++i)
			if (a[i].second < 0)
				enter_subway(a[i].first, -a[i].second);
			else
				leave_subway(a[i].first, a[i].second);

		if (total_paid > must_pay)
			must_pay += mod;

		cout << "Case #" << TT << ": " << must_pay - total_paid << endl;
	}
	return 0;
}