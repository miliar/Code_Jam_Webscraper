#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long int lli;

class magicalmarveloustour
{
	private:
		int n, p, q, r, s;

		int trancnt(int i) {
			return (i * p + q) % r + s;
		}

	public:
		magicalmarveloustour() {}

		void input() {
			cin >> n >> p >> q >> r >> s;
		}

		string solve() {
			ostringstream oss;
			vector<lli> psum;
			psum.reserve(n + 1);
			lli sum = 0l;
			for (int i = 0; i < n; ++i) {
				psum.push_back(sum);
				sum += trancnt(i);
			}
			psum.push_back(sum);
			lli maxseg = sum;
			for (int i = 0; i <= n; ++i) {
				lli rem = sum - psum.at(i);
				int b = 0, e = i, m;
				while (b < e - 1) {
					m = b + (e - b) / 2;
					lli mh = psum.at(m);
					if (mh < sum - rem - mh) {
						b = m;
					} else {
						e = m;
					}
				}
				lli mh = psum.at(b);
				maxseg = min(maxseg, max(rem, max(mh, sum - rem - mh)));
				if (b > 0) {
					mh = psum.at(b - 1);
					maxseg = min(maxseg, max(rem, max(mh, sum - rem - mh)));
				}
				if (b < i) {
					mh = psum.at(b + 1);
					maxseg = min(maxseg, max(rem, max(mh, sum - rem - mh)));
				}
			}
			//cout << sum << endl;
			//cout << (sum - maxseg) << endl;
			oss.setf(ios::fixed);
			oss.precision(10);
			oss << (static_cast<long double>(sum - maxseg) / sum);
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		magicalmarveloustour task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
