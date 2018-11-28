#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class dontbreakthenile
{
	private:
		vector<pair<int, int> > directions;

		struct building
		{
			int wb, we;
			int hb, he;

			building(int wb_, int we_, int hb_, int he_) : wb(wb_), we(we_), hb(hb_), he(he_) {}
		};

		int w, h;
		int b;
		vector<building> bds;

		bool trydfs(vector<vector<bool> > &map, int x, int y, int ld) {
			if ((x < 0) || (y < 0) || (x >= w) || (y >= h)) {
				return false;
			}
			if (map.at(x).at(y)) {
				return false;
			}
			map.at(x).at(y) = true;
			if (y >= h - 1) {
				return true;
			}
			for (int dc = 0, d = (ld + 1) % 4; dc < 3; ++dc, d = (d - 1 + 4) % 4) {
				if (trydfs(map, x + directions.at(d).first, y + directions.at(d).second, d)) {
					return true;
				}
			}
			//map.at(x).at(y) = false;
			return false;
		}
	public:
		dontbreakthenile() {
			directions.reserve(4);
			directions.push_back(make_pair(0, 1)); // up
			directions.push_back(make_pair(-1, 0)); // left
			directions.push_back(make_pair(0, -1)); // down
			directions.push_back(make_pair(1, 0)); // right
		}

		void input() {
			cin >> w >> h >> b;
			bds.reserve(b);
			int x0, y0, x1, y1;
			for (int i = 0; i < b; ++i) {
				cin >> x0 >> y0 >> x1 >> y1;
				bds.push_back(building(x0, x1, y0, y1));
			}
		}

		string solve() {
			ostringstream oss;
			vector<vector<bool> > map(w, vector<bool>(h, false));
			for (vector<building>::iterator bi = bds.begin(); bi < bds.end(); ++bi) {
				for (int i = bi->wb; i <= bi->we; ++i) {
					for (int j = bi->hb; j <= bi->he; ++j) {
						map.at(i).at(j) = true;
					}
				}
			}
			int sol = 0;
			/*for (int j = h - 1; j >= 0; --j) {
				for (int i = 0; i < w; ++i) {
					cerr << (map.at(i).at(j)? '#' : '.');
				}
				cerr << endl;
			}
			cerr << endl;*/
			for (int i = 0; i < w; ++i) {
				if (trydfs(map, i, 0, 0)) {
					++sol;
				}
				//cerr << sol << endl;
				/*for (int j = h - 1; j >= 0; --j) {
					for (int i = 0; i < w; ++i) {
						cerr << (map.at(i).at(j)? '#' : '.');
					}
					cerr << endl;
				}
				cerr << endl;*/
			}
			oss << sol;
			return oss.str();
		}
};

int main(void) {
	int nt;
	cin >> nt;
	for (int znj = 0; znj < nt; ++znj) {
		dontbreakthenile task;
		task.input();
		cout << "Case #" << (znj + 1) << ": " << task.solve() << endl;
	}
	return 0;
}
