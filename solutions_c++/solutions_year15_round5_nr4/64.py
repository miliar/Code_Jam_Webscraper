#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
using namespace std;

typedef long long int64;

int getLog(int64 x) {
	int ret = 0;
	while (x > 1)
		x /= 2, ++ret;
	return ret;
}

vector<pair<int64, int64> > divide(vector<pair<int64, int64> > poly, int64 v) {
	//poly / (1+x^v)
	sort(poly.begin(), poly.end());
	map<int64, int64> op, np;
	for (int i = 0; i < poly.size(); ++i) {
		op[poly[i].first] = poly[i].second;
	}
	for (int i = poly.size() - 1; i >= 0; --i) {
		np[poly[i].first] = op[poly[i].first + v] - np[poly[i].first + v];
	}
	poly.clear();
	for (map<int64, int64>::iterator e = np.begin(); e != np.end(); ++e) {
		if (e->second > 0)
			poly.push_back(make_pair(e->first, e->second));
	}
	return poly;
}

int main() {
	int nT;
	cin >> nT;
	for (int nc = 1; nc <= nT; ++nc) {
		vector<int64> ret;
		int n;
		cin >> n;
		vector<pair<int64, int64> > poly(n); //pow,cof
		for (int i = 0; i < n; ++i) {
			cin >> poly[i].first;
		}
		for (int i = 0; i < n; ++i) {
			cin >> poly[i].second;
		}
		sort(poly.begin(), poly.end());
		int64 C = poly[0].first;
		for (int i = 0; i < poly.size(); ++i) {
			poly[i].first -= C;
		}
		int64 d = poly[0].second;
		int numZero = getLog(d);
		for (int i = 0; i < numZero; ++i) {
			ret.push_back(0);
		}

		for (int i = 0; i < n; ++i) {
			poly[i].second /= d;
		}
		//now, we assume there are no zero!
		vector<pair<int64, int64> > cur = poly;
		while (cur.size() > 1) {
//			cout << cur.size() << endl;
//			for (int i = 0; i < cur.size(); ++i) {
//				cout << cur[i].first << " " << cur[i].second << endl;
//			}
			ret.push_back(cur[1].first);
			int64 v = cur[1].first;
			cur = divide(cur, v);
		}
		sort(ret.rbegin(), ret.rend());
		C *= -1;

		cur = poly;
		for (int i = 0; i < ret.size(); ++i) {
			int64 v = ret[i];
			if (v == 0)
				continue;
			cur = divide(poly, v);
			for (int i = 0; i < cur.size(); ++i) {
				if (cur[i].first == C - ret[i]) {
					C -= ret[i];
					ret[i] *= -1;
				}
			}
		}

		sort(ret.begin(), ret.end());
		printf("Case #%d:", nc);
		for (int i = 0; i < ret.size(); ++i) {
			cout << " " << ret[i];
		}
		cout << endl;
	}
}
