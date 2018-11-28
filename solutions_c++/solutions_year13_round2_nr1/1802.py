#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
#include <numeric>
using namespace std;

ofstream out("out.txt");


map<int, int> cache;

int ins(long long a, long long &b, int target) {
	b = a;
	int u = 0;
	while (b <= target) {
		b *= 2;
		b -= 1;
		u++;
	}
	return u;
}

int next(vector<int> m, long long a) {
//	vector <int> v = m;
	int best = m.size();

	if (a == 1) return best;
	int index = accumulate(m.begin(),m.end(),0);
	if (cache.count(index) > 0) return cache.at(index);
	if (!best) return 0;
	long long b;
	int ii = ins(a, b, m.at(0));

	while (!m.empty() && b > m.at(0)) {
		b+=m.at(0);
		m.erase(m.begin());
	}
//	cout << best << endl;
	best = min(best, next(m, b) + ii);
//	cout << best << endl;
//	for (int i = 0; i < v.size(); i++) {
//		cout << v.at(i) << " ";
//	}
//	cout << ": " << best << endl;
	cache[index] = best;
	return best;
}

int main() {
	ifstream f("A-large (1).in");
	int T;
	f >> T;

	for (int x = 0; x < T; x++) {
		cache.clear();
		int n, used = 0;
		long long a;
		f >> a >> n;
		vector<int> motes;
		for (int i = 0; i < n; i++) {
			int q;
			f >> q;
			motes.push_back(q);

		}

		sort(motes.begin(), motes.end());


		out << "Case #" << x + 1 << ": " << next(motes, a) << endl;

	}

	return 0;
}
