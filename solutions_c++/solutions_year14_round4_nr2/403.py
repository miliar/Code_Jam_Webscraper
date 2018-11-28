#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class upanddown
{
	private:
		int n;
		vector<int> ats;

	public:
		upanddown() {}

		void input() {
			cin >> n;
			ats.resize(n);
			for (int i = 0; i < n; ++i) {
				cin >> ats.at(i);
			}
		}

		string solve() {
			ostringstream oss;
			int swc = 0;
			int lb = 0, ub = n;
			for (int i = 0; i < n; ++i) {
				int m = ats.at(lb);
				int mi = lb;
				for (int j = lb + 1; j < ub; ++j) {
					if (ats.at(j) < m) {
						m = ats.at(j);
						mi = j;
					}
				}
				if (mi - lb <= ub - mi - 1) {
					for (int j = mi; j > lb; --j) {
						swap(ats.at(j), ats.at(j - 1));
						++swc;
					}
					++lb;
				} else {
					for (int j = mi; j < ub - 1; ++j) {
						swap(ats.at(j), ats.at(j + 1));
						++swc;
					}
					--ub;
				}
			}
			oss << swc;
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		upanddown task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
