#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class magictrick
{
	private:
		const int RN, CN;

		int ri1, ri2;
		vector<int> r1, r2;

		void inputrow(int &ri, vector<int> &r) {
			cin >> ri;
			--ri;
			r.reserve(CN);
			int x;
			for (int i = 0; i < RN; ++i) {
				for (int j = 0; j < CN; ++j) {
					cin >> x;
					if (i == ri) {
						r.push_back(x);
					}
				}
			}
		}

	public:
		magictrick() : RN(4), CN(4) {}

		void input() {
			inputrow(ri1, r1);
			inputrow(ri2, r2);
		}

		string solve() {
			ostringstream oss;
			int mc = 0;
			int cs = -1;
			for (vector<int>::iterator i1 = r1.begin(); i1 < r1.end(); ++i1) {
				for (vector<int>::iterator i2 = r2.begin(); i2 < r2.end(); ++i2) {
					if (*i1 == *i2) {
						++mc;
						cs = *i1;
					}
				}
			}
			if (mc == 1) {
				oss << cs;
			} else if (mc > 1) {
				oss << "Bad magician!";
			} else {
				oss << "Volunteer cheated!";
			}
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		magictrick task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
