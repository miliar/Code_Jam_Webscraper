#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class erdosszekeres
{
	private:
		int n;
		vector<int> asc, desc;

	public:
		void input() {
			cin >> n;
			asc.resize(n);
			for (int f = 0; f < n; ++f) {
				cin >> asc.at(f);
			}
			desc.resize(n);
			for (int f = 0; f < n; ++f) {
				cin >> desc.at(f);
			}
		}

		string solve() {
			vector<vector<int> > conds(n);
			for (int f = 0; f < n; ++f) {
				for (int g = f + 1; g < n; ++g) {
					if (asc.at(g) <= asc.at(f)) {
						conds.at(g).push_back(f);
					}
				}
				for (int g = f - 1; g >= 0; --g) {
					if (desc.at(g) + 1 == desc.at(f)) {
						conds.at(g).push_back(f);
						break;
					}
				}
			}
			for (int f = 0; f < n; ++f) {
				for (int g = f - 1; g >= 0; --g) {
					if (desc.at(g) <= desc.at(f)) {
						conds.at(g).push_back(f);
					}
				}
				for (int g = f + 1; g < n; ++g) {
					if (desc.at(g) + 1 == desc.at(f)) {
						conds.at(g).push_back(f);
						break;
					}
				}
			}
			vector<int> ecnt(n, 0);
			for (int f = 0; f < n; ++f) {
				sort(conds.at(f).begin(), conds.at(f).end());
				conds.at(f).erase(unique(conds.at(f).begin(), conds.at(f).end()), conds.at(f).end());
				for (unsigned int g = 0; g < conds.at(f).size(); ++g) {
					++ecnt.at(conds.at(f).at(g));
				}
			}
			vector<int> sol(n, -1);
			for (int l = 1; l <= n; ++l) {
				for (int f = 0; f < n; ++f) {
					if ((sol.at(f) < 0) && (ecnt.at(f) == 0)) {
						for (unsigned int g = 0; g < conds.at(f).size(); ++g) {
							--ecnt.at(conds.at(f).at(g));
						}
						sol.at(f) = l;
						break;
					}
				}
			}
			ostringstream oss;
			oss << sol.at(0);
			for (int f = 1; f < n; ++f) {
				oss << ' ' << sol.at(f);
			}
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		erdosszekeres task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
