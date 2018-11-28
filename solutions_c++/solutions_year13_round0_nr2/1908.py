#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class lawnmower
{
	private:
		int n, m;
		vector<vector<int> > tgh;

		int maxheight(int sx, int sy, int dx, int dy, int dc) {
			int mxht = 0;
			for (int d = 0; d < dc; ++d) {
				int ch = tgh.at(sx + d * dx).at(sy + d * dy);
				mxht = max(mxht, ch);
			}
			return mxht;
		}

	public:
		void input() {
			cin >> n >> m;
			tgh.resize(n);
			for (int f = 0; f < n; ++f) {
				tgh.at(f).resize(m);
				for (int g = 0; g < m; ++g) {
					cin >> tgh.at(f).at(g);
				}
			}
		}

		bool solve() {
			vector<int> mxhtx(n, 0);
			for (int f = 0; f < n; ++f) {
				mxhtx.at(f) = maxheight(f, 0, 0, 1, m);
			}
			vector<int> mxhty(m, 0);
			for (int f = 0; f < m; ++f) {
				mxhty.at(f) = maxheight(0, f, 1, 0, n);
			}
			for (int f = 0; f < n; ++f) {
				for (int g = 0; g < m; ++g) {
					int ch = tgh.at(f).at(g);
					if ((ch < mxhtx.at(f)) && (ch < mxhty.at(g))) {
						return false;
					}
				}
			}
			return true;
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		lawnmower task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << (task.solve()? "YES" : "NO") << endl;
	}
	return 0;
}
