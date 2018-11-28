#if 1
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <unordered_set>
using namespace std;

struct Chest {
	int type, numKeys;
	vector<int> keys;
	int index;
};

typedef bitset<200> Flags;

bool calc(vector<int> &v, const vector<Chest> &chests, vector<int> &keys,
		Flags &opened, unordered_set<Flags> &failed) {
	if (failed.find(opened) != failed.end())
		return false;
	if (opened == Flags((1 << chests.size()) - 1))
		return true;
	for (auto &chest : chests) {
		if (opened[chest.index])
			continue;
		if (keys[chest.type] > 0) {
			--keys[chest.type];
			for (auto k : chest.keys)
				++keys[k];
			v.push_back(chest.index);
			if (calc(v, chests, keys, opened.set(chest.index), failed))
				return true;
			opened.reset(chest.index);
			v.pop_back();
			++keys[chest.type];
			for (auto k : chest.keys)
				--keys[k];
		}
	}
	failed.insert(opened);
	return false;
}

void solve(istream &in, ostream &out) {
	int T;
	in >> T;

	for (int t = 1; t <= T; ++t) {
		int K, N;
		in >> K >> N;

		Flags opened;
		vector<int> keys(201);
		for (int k = 0; k < K; ++k) {
			int a;
			in >> a;
			++keys[a];
		}

		vector<Chest> chests(N);
		for (int i = 0; i < N; ++i) {
			Chest &c = chests[i];
			in >> c.type >> c.numKeys;
			c.keys.resize(c.numKeys);
			for (int j = 0; j < c.numKeys; ++j) {
				int k;
				in >> k;
				c.keys[j] = k;
			}
			c.index = i;
		}

		vector<int> v;
		unordered_set<Flags> failed;
		if (!calc(v, chests, keys, opened, failed)) {
			out << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		out << "Case #" << t << ":";
		for (auto c : v)
			out << ' ' << c + 1;
		out << endl;
	}
}

int main() {
	solve(cin, cout);
	return 0;
}
#endif
