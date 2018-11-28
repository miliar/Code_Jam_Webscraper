#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <functional>

using namespace std;

struct route {
	int first, last, p;
};

struct ev {
	bool type;
	int pos, index;

	ev(bool type, int pos, int index) : type(type), pos(pos), index(index) {}

	friend bool operator<(const ev & a, const ev & b) {
		return a.pos < b.pos || (a.pos == b.pos && a.type == true);
	}
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	const int MOD = 1000002013ll;
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n, m;
		cin >> n >> m;
		vector < route > A(m);
		vector < ev > events;
		long long expected = 0, real = 0;
		for(int i = 0; i < m; ++i) {
			cin >> A[i].first >> A[i].last >> A[i].p;
			events.emplace_back(ev(true, A[i].first, i));
			events.emplace_back(ev(false, A[i].last, i));
			int k = A[i].last - A[i].first;
			long long tmp = ((1ll * k) * (2ll * n - k + 1)) / 2;
			tmp %= MOD;
			tmp = (tmp * A[i].p) % MOD;
			expected = (expected + tmp) % MOD;
		}
		sort(events.begin(), events.end());
		stack < route > st;
		for(int i = 0; i < 2 * m; ++i) {
			if(events[i].type) {
				st.push(A[events[i].index]);
			}
			else {
				int count = A[events[i].index].p;
				while(count > 0) {
					route v = st.top();
					st.pop();
					int k = events[i].pos - v.first;
					long long tmp = ((1ll * k) * (2ll * n - k + 1)) / 2;
					tmp %= MOD;
					if(v.p > count) {
						v.p -= count;
						st.push(v);
						tmp = (tmp * count) % MOD;
						real = (real + tmp) % MOD;
						count = 0;
					}
					else {
						tmp = (tmp * v.p) % MOD;
						real = (real + tmp) % MOD;
						count -= v.p;
					}
				}
			}
		}

		long long answer = (MOD + expected - real) % MOD;
		cout << "Case #" << t << ": " << answer << endl;
	}
}