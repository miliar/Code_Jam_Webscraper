#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long int lli;

class ticketswapping
{
	private:
		struct ticketevent
		{
			int stn;
			bool exit;
			int delta;

			ticketevent(int stn_, bool exit_, int delta_) : stn(stn_), exit(exit_), delta(delta_) {}
			const bool operator<(const ticketevent &other) const {
				return (stn < other.stn) || ((stn == other.stn) && (exit < other.exit));
			}
		};

		int n, m;
		vector<ticketevent> events;
		int fairsum;

		const int mod;

		lli tripcost(lli distance) {
			return (distance * (2 * n - distance + 1)) / 2;
		}

	public:
		ticketswapping() : mod(1000002013) {}

		void input() {
			cin >> n >> m;
			events.reserve(2 * m);
			fairsum = 0;
			int o, e, p;
			for (int i = 0; i < m; ++i) {
				cin >> o >> e >> p;
				events.push_back(ticketevent(o, false, p));
				events.push_back(ticketevent(e, true, p));
				fairsum += (p * tripcost(e - o)) % mod;
				fairsum %= mod;
			}
		}

		int solve() {
			sort(events.begin(), events.end());
			priority_queue<pair<int, int> > travelling;
			int sol = 0;
			for (vector<ticketevent>::iterator ei = events.begin(); ei < events.end(); ++ei) {
				if (ei->exit) {
					while (ei->delta > 0) {
						pair<int, int> cpp = travelling.top();
						travelling.pop();
						if (cpp.second > ei->delta) {
							sol += (ei->delta * tripcost(ei->stn - cpp.first)) % mod;
							sol %= mod;
							cpp.second -= ei->delta;
							ei->delta = 0;
							travelling.push(cpp);
						} else {
							sol += (cpp.second * tripcost(ei->stn - cpp.first)) % mod;
							sol %= mod;
							ei->delta -= cpp.second;
						}
					}
				} else {
					travelling.push(make_pair(ei->stn, ei->delta));
				}
			}
			return (fairsum - sol + mod) % mod;
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		ticketswapping task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
