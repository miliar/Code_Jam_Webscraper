#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	string s;
	getline(cin, s);
	istringstream iss0(s);
	int T = 0;
	iss0 >> T;

	for (int t = 0; t < T; t++) {
		cerr << t << endl;
		string s;
		getline(cin, s);
		istringstream iss1(s);
		int N = 0;
		iss1 >> N;

		vector < vector<int> > v(N);
		map<string,int> found;
		int idx = 0;
		for (int i = 0; i < N; i++) {
			string s;
			getline(cin, s);
			istringstream iss(s);
			while (!iss.eof()) {
				string w;
				iss >> w;
				auto it = found.find(w);
				if (it == found.end()) {
					v[i].push_back(++idx);
					found[w] = idx;
				}
				else {
					v[i].push_back(it->second);
				}
			}
		}

		auto E0 = v[0];
		auto F0 = v[1];
		if (N == 2) {
			vector<int> c;
			sort(E0.begin(), E0.end());
			sort(F0.begin(), F0.end());
			set_intersection(E0.begin(), E0.end(), F0.begin(), F0.end(), back_inserter(c));
			printf("Case #%d: %ld\n", t + 1, (int)c.size());
			continue;
		}

		auto ans = found.size();
		auto NN = (1 << (N - 2));
#pragma omp parallel for
		for (int i = 0; i < NN; i++) {
			auto E = E0;
			auto F = F0;
			for (int j = 0; j < N - 2; j++) {
				if (i&(1 << j)) {
					E.insert(E.end(), v[j+2].begin(), v[j+2].end());
				}
				else {
					F.insert(F.end(), v[j+2].begin(), v[j+2].end());
				}
			}
			vector<int> c;
			sort(E.begin(), E.end());
			sort(F.begin(), F.end());
			E.erase(unique(E.begin(), E.end()), E.end());
			F.erase(unique(F.begin(), F.end()), F.end());
			set_intersection(E.begin(), E.end(), F.begin(), F.end(), back_inserter(c));
#pragma omp critical
			ans = min(ans, c.size());
		}

		printf("Case #%d: %ld\n", t + 1, (int)ans);
	}

	return 0;
}
