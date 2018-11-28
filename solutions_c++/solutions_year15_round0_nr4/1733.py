#include <iostream>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <unordered_set>


using namespace std;


vector<vector<pair<int, int> > > v[4];
bool b[100][100];
int s = 0;
int r, c;


bool get(int i) {
	bool bbb = true;
	for (int g = 0; g < r; g++) {
		for (int g1 = 0; g1 < c; g1++) {
			if (!b[g][g1]) {
				bbb = false;
			}
		}
	}
	if (bbb) {
		return true;
	}
	for (int j = 0; j < 4; j++) {
		for (int g = 0; g < r; g++) {
			for (int g1 = 0; g1 < c; g1++) {
				bool bb = true;
				for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
					if (v[s][i][g2].first + g >= r || v[s][i][g2].second + g1 >= c) {
						bb = false;
						break;
					}
					if (b[v[s][i][g2].first + g][v[s][i][g2].second + g1]) {
						bb = false;
						break;
					}
				}
				if (bb) {
					//cout << "opa" << endl;
					vector<pair<int, int> > v2;
					for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
						b[v[s][i][g2].first + g][v[s][i][g2].second + g1] = true;
						v2.push_back(make_pair(v[s][i][g2].first + g, v[s][i][g2].second + g1));
					}
					for (int g2 = 0; g2 < (int)v[s].size(); g2++) {
						if (get(g2)) {
							for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
								b[v2[g2].first][v2[g2].second] = false;
							}
							return true;
						}
					}
					for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
						b[v2[g2].first][v2[g2].second] = false;
					}
				}
			}
		}
		int y = 0;
		for (int g = 0; g < (int)v[s][i].size(); g++) {
			y = max(y, v[s][i][g].second);
		}
		for (int g = 0; g < (int)v[s][i].size(); g++) {
			int yy = v[s][i][g].second;
			v[s][i][g].second = v[s][i][g].first;
			v[s][i][g].first = y - yy;
		}
		//cout << "opa" << endl;
	}
	int y = 0;
	for (int g = 0; g < (int)v[s][i].size(); g++) {
		y = max(y, v[s][i][g].second);
	}
	for (int g = 0; g < (int)v[s][i].size(); g++) {
		v[s][i][g].second = y - v[s][i][g].second;
	}
	for (int j = 0; j < 4; j++) {
		for (int g = 0; g < r; g++) {
			for (int g1 = 0; g1 < c; g1++) {
				bool bb = true;
				for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
					if (v[s][i][g2].first + g >= r || v[s][i][g2].second + g1 >= c) {
						bb = false;
						break;
					}
					if (b[v[s][i][g2].first + g][v[s][i][g2].second + g1]) {
						bb = false;
						break;
					}
				}
				if (bb) {
					//cout << "opa" << endl;
					vector<pair<int, int> > v2;
					for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
						b[v[s][i][g2].first + g][v[s][i][g2].second + g1] = true;
						v2.push_back(make_pair(v[s][i][g2].first + g, v[s][i][g2].second + g1));
					}
					for (int g2 = 0; g2 < (int)v[s].size(); g2++) {
						if (get(g2)) {
							for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
								b[v2[g2].first][v2[g2].second] = false;
							}
							return true;
						}
					}
					for (int g2 = 0; g2 < (int)v[s][i].size(); g2++) {
						b[v2[g2].first][v2[g2].second] = false;
					}
				}
			}
		}
		int y = 0;
		for (int g = 0; g < (int)v[s][i].size(); g++) {
			y = max(y, v[s][i][g].second);
		}
		for (int g = 0; g < (int)v[s][i].size(); g++) {
			int yy = v[s][i][g].second;
			v[s][i][g].second = v[s][i][g].first;
			v[s][i][g].first = y - yy;
		}
		//cout << "opa" << endl;
	}
	return false;
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<pair<int, int> > v1;
	v1.push_back(make_pair(0, 0));
	v[0].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v[1].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(0, 2));
	v[2].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(1, 0));
	v[2].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(1, 0));
	v1.push_back(make_pair(1, 1));
	v[3].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(0, 2));
	v1.push_back(make_pair(0, 3));
	v[3].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(0, 2));
	v1.push_back(make_pair(1, 1));
	v[3].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(0, 2));
	v1.push_back(make_pair(1, 2));
	v[3].push_back(v1);
	v1.clear();
	v1.push_back(make_pair(0, 0));
	v1.push_back(make_pair(0, 1));
	v1.push_back(make_pair(1, 1));
	v1.push_back(make_pair(1, 2));
	v[3].push_back(v1);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int x;
		cin >> x >> c >> r;
		 // for (int h = 0; h < r; h++) {
			// 				for (int f = 0; f < c; f++) {
			// 					cout << b[h][f] << ' ';
			// 				}
			// 				cout << endl;
			// 			}
		if ((c * r) % x != 0) {
			printf("Case #%d: RICHARD\n", i + 1);
			continue;
		}
		s = x - 1;
		bool bb = true;
		for (int j = 0; j < (int)v[x - 1].size(); j++) {
			if (!get(j)) {
				bb = false;
				printf("Case #%d: RICHARD\n", i + 1);
				break;
			}
		}
		if (bb) {
			printf("Case #%d: GABRIEL\n", i + 1);
		}
		//cout << "opa" << endl;
		// for (int h = 0; h < r; h++) {
		// 					for (int f = 0; f < c; f++) {
		// 						cout << b[h][f] << ' ';
		// 					}
		// 					cout << endl;
		// 				}
	}
    return 0;
}
