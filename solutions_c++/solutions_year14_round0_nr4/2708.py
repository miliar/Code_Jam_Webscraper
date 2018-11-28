#include <iostream>
#include <cstdio>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class deceitfulwar
{
	private:
		int n;
		vector<double> nb, kb;

		int solcheat() {
			deque<double> nd(nb.begin(), nb.end()), kd(kb.begin(), kb.end());
			int sol = 0;
			for (int i = 0; i < n; ++i) {
				if (nd.front() > kd.front()) {
					nd.pop_front();
					kd.pop_front();
					++sol;
				} else {
					nd.pop_front();
					kd.pop_back();
				}
			}
			return sol;
		}

		int solfair() {
			deque<double> nd(nb.begin(), nb.end()), kd(kb.begin(), kb.end());
			int sol = 0;
			for (int i = 0; i < n; ++i) {
				while ((!(kd.empty())) && (nd.front() > kd.front())) {
					kd.pop_front();
				}
				if (kd.empty()) {
					++sol;
				} else {
					kd.pop_front();
				}
				nd.pop_front();
			}
			return sol;
		}

	public:
		deceitfulwar() {}

		void input() {
			double w;
			cin >> n;
			nb.reserve(n);
			for (int i = 0; i < n; ++i) {
				cin >> w;
				nb.push_back(w);
			}
			kb.reserve(n);
			for (int i = 0; i < n; ++i) {
				cin >> w;
				kb.push_back(w);
			}
		}

		string solve() {
			ostringstream oss;
			sort(nb.begin(), nb.end());
			sort(kb.begin(), kb.end());
			oss << solcheat() << ' ' << solfair();
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		deceitfulwar task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
