#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class triesharding
{
	private:
		int m;
		vector<string> strs;
		int n;

	public:
		triesharding() {}

		void input() {
			cin >> m >> n;
			strs.resize(m);
			for (int i = 0; i < m; ++i) {
				cin >> strs.at(i);
				strs.at(i) = "$" + strs.at(i);
			}
		}

		string solve() {
			ostringstream oss;
			int maxnod = -1;
			int maxways = 0;
			vector<int> assign(m, 0);
			while (true) {
				int nodes = 0;
				for (int i = 0; i < m; ++i) {
					int bmatch = 0;
					for (int j = 0; j < i; ++j) {
						if (assign.at(j) != assign.at(i)) {
							continue;
						}
						int k = 0;
						for (; k < static_cast<int>(min(strs.at(j).size(), strs.at(i).size())); ++k) {
							if (strs.at(j).at(k) != strs.at(i).at(k)) {
								break;
							}
						}
						bmatch = max(bmatch, k);
					}
					nodes += strs.at(i).size() - bmatch;
				}
				if (maxnod < nodes) {
					maxnod = nodes;
					maxways = 1;
				} else if (maxnod == nodes) {
					++maxways;
				}
				int i = 0;
				for (; i < m; ++i) {
					++assign.at(i);
					if (assign.at(i) >= n) {
						assign.at(i) = 0;
					} else {
						break;
					}
				}
				if (i >= m) {
					break;
				}
			}
			oss << maxnod << ' ' << maxways;
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		triesharding task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
