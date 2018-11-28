#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class datapacking
{
	private:
		int n;
		vector<int> sizes;
		int cap;

	public:
		datapacking() {}

		void input() {
			cin >> n >> cap;
			sizes.resize(n);
			for (int i = 0; i < n; ++i) {
				cin >> sizes.at(i);
			}
		}

		string solve() {
			ostringstream oss;
			int ndr = 0;
			vector<bool> used(n, false);
			sort(sizes.begin(), sizes.end());
			for (int i = sizes.size() - 1; i >= 0; --i) {
				if (used.at(i)) {
					continue;
				}
				used.at(i) = true;
				++ndr;
				int rcap = cap - sizes.at(i);
				for (int j = i - 1; j >= 0; --j) {
					if (used.at(j)) {
						continue;
					}
					if (sizes.at(j) <= rcap) {
						used.at(j) = true;
						break;
					}
				}
			}
			oss << ndr;
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		datapacking task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
