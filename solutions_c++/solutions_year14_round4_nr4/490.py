#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <iterator>
#include <unordered_set>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		int M, N;
		in >> M >> N;
		vector<string> strings;
		for (int j = 0; j < M; ++j) {
			string t;
			in >> t;
			strings.push_back(t);
		}
		int pows[9];
		for (int a = 0; a < 9; ++a) {
			pows[a] = pow(N, a);
		}
		int most = 0, count = 0;
		unordered_set<string> buckets[4];
		for (int k = 0; k < N; ++k) {
			buckets[k] = unordered_set<string>();
		}
		for (int j = 0; j < pows[M]; ++j) {
			for (int k = 0; k < N; ++k) {
				buckets[k].clear();
			}

			int nums[4] = { 0 };
			for (int k = 0; k < M; ++k) {
				++nums[(j / pows[k]) % N];
			}
			bool good = true;
			for (int k = 0; k < N; ++k) {
				good = good && nums[k];
			}
			if (!good) {
				continue;
			}

			for (int k = 0; k < M; ++k) {
				int b = (j / pows[k]) % N;
				for (int s = strings[k].length(); s >= 0; --s) {
					auto ret = buckets[b].insert(strings[k].substr(0, s));
					if (!ret.second) {
						break;
					}
				}
			}
			int tot = 0;
			for (int k = 0; k < N; ++k) {
				tot += buckets[k].size();
			}
			if (tot >= most) {
				if (tot > most) {
					most = tot;
					count = 0;
				}
				++count;
			}
		}
		out << "Case #" << (i + 1) << ": " << most << " " << count << endl;
	}
}