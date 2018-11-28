#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class lasthit
{
	private:
		int p, q, n;
		vector<int> mhit, mgold;

		int towerkillhits(int hp) {
			return hp / q + ((hp % q != 0)? 1 : 0);
		}

		int dianakillhits(int hp) {
			return hp / p + ((hp % p != 0)? 1 : 0);
		}

	public:
		lasthit() {}

		void input() {
			cin >> p >> q >> n;
			mhit.resize(n);
			mgold.resize(n);
			for (int i = 0; i < n; ++i) {
				cin >> mhit.at(i) >> mgold.at(i);
			}
		}

		string solve() {
			ostringstream oss;
			int mp = 1;
			for (int i = 0; i < n; ++i) {
				mp += towerkillhits(mhit.at(i));
			}
			vector<vector<int> > dp(n + 1, vector<int>(mp + 1, 0));
			for (int i = n - 1; i >= 0; --i) {
				for (int j = 0; j <= mp; ++j) {
					int tkh = towerkillhits(mhit.at(i));
					int njnk = j + tkh;
					int njk = j + (tkh - 1) - dianakillhits(mhit.at(i) - (tkh - 1) * q);
					for (int k = 0; k <= min(mp, njnk); ++k) {
						dp.at(i).at(j) = max(dp.at(i).at(j), dp.at(i + 1).at(k) + ((k <= njk)? mgold.at(i) : 0));
					}
				}
			}
			oss << dp.at(0).at(1);
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		lasthit task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
