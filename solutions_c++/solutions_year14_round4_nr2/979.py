#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int>::iterator iter;

class UpDown {
public:
	int sortUp(vector<int> &v, int n) {
		int c = 0;
		for(int i = n - 1; i > 0; --i) {
			for(int j = 0; j < i; ++j) {
				if(v[j] > v[j+1]) {
					swap(v[j], v[j + 1]);
					++c;
				}
			}
		}
		return c;
	}

	int sortDown(vector<int> &v, int n) {
		int c = 0;
		for(int i = v.size() - 1; i > n; --i) {
			for(int j = n; j < i; ++j) {
				if(v[j] < v[j + 1]) {
					swap(v[j], v[j + 1]);
					++c;
				}
			}
		}
		return c;
	}

	void go(istream &in, ostream &out) {
		int t;
		in >> t;

		for(int i = 1; i <= t; ++i) {
			int n, a;
			in >> n;

			vector<int> as;
			for(int j = 0; j < n; ++j) {
				in >> a;
				as.push_back(a);
			}

			//int m = 999999999;
			//vector<int> best;
			//for(int k = 0; k <= n; ++k) {
			//	vector<int> temp = as;
			//	int c = sortUp(temp, k) + sortDown(temp, k);
			//	if(c < m) {
			//		m = c;
			//		best = temp;
			//	}
			//}

			int c = 0;
			int u = 0, v = n - 1;
			for(int j = 0; j < n; ++j) {
				int m = u;
				for(int k = u+1; k <= v; ++k) {
					if(as[k] < as[m])
						m = k;
				}

				if(m - u < v - m) {
					c += m - u;
					for(int k = m; k > u; --k)
						swap(as[k], as[k - 1]);
					++u;
				} else {
					c += v - m;
					for(int k = m; k < v; ++k)
						swap(as[k], as[k + 1]);
					--v;
				}
			}

			out << "Case #" << i << ": " << c << endl;
			//for(int j = 0; j < as.size(); ++j)
			//	out << as[j] << " ";
			//out << endl;
		}
	}
};