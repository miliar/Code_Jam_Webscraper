
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <bitset>
#include <map>
#include <set>
using namespace std;

int64_t cross(int &ol, int &el, int &oR, int &eR) {
	int ool = ol, oel = el, oor = oR, oer = eR;
	if (ol == oR) {
		if (eR < el)
			swap(el, eR);
		return 0;
	}
	if (el == eR) {
		if (ol < oR)
			swap(ol, oR);
		return 0;
	}

	if (el < oR || eR < ol)
		return 0;

	if (ol == el)
		return 0;
	if (oR == eR) {
		swap(ol, oR);
		swap(el, eR);
		return 0;
	}
	if (oR < ol && el < eR)
		return 0;
	if (ol < oR && eR < el) {
		swap(ol, oR);
		swap(el, eR);
		return 0;
	}

	int64_t nl = el - ol;
	int64_t nr = eR - oR;

	if (ol < oR && oR <= el)
		swap(el, eR);
	if (oR < ol && ol <= eR)
		swap(el, eR);

	int64_t nR = eR - oR;
	int64_t nL = el - ol;

	auto r = -(nl + 1) * nl / 2 - (nr + 1) * nr / 2 + (nL + 1) * nL / 2
			+ (nR + 1) * nR / 2;
	if (r < 0) {
		cout << ool << ',' << oel << ',' << oor << ',' << oer << endl;
		cout << "after:" << ol << ',' << el << ',' << oR << ',' << eR << endl;
		exit(0);
	}
	return r;

}

int calc(vector<int> &o, vector<int> &e) {
	int res = 0;
	while (!o.empty()) {
//		cout << o.size() << endl;
		int oR = o.back(), eR = e.back();
		o.pop_back(), e.pop_back();
		if (oR == eR)
			continue;

		bool updated = false;

		for (size_t i = 0; i < o.size(); ++i) {
//			res += cross(o[i], e[i], oR, eR);
			int r = cross(oR, eR, o[i], e[i]);
			if (r > 0) {
				res += r;
//			cout << "res:" << res << endl;

				updated = true;
			}
		}
		if (updated)
			o.push_back(oR), e.push_back(eR);
	}
	return res;
}

void solve(istream &in, ostream &out) {
	int T;
	in >> T;

	for (int t = 1; t <= T; ++t) {
//		cout << "Case: #" << t << endl;
		int N, M;
		in >> N >> M;

		vector<int> o, e;
		for (int i = 0; i < M; ++i) {
			int oi, ei, p;
			in >> oi >> ei >> p;
			for (int j = 0; j < p; ++j)
				o.push_back(oi), e.push_back(ei);
		}

		out << "Case #" << t << ": " << calc(o, e) << endl;
	}
}

int main() {
	solve(cin, cout);
	return 0;
}
