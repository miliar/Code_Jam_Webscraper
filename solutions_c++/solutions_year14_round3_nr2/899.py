#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
#include <queue>
using namespace std;

int T, n;
vector<string> v;
vector<int> idx;
string s;
const int l = 200;
bool tf[l];

void print() {
	// return;

	for (int i = 0; i < idx.size(); i++) {
		cout << v[idx[i]] << ' ';
	}
	cout << endl;
}

int main() {
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		printf("Case #%d: ", cc);

		cin >> n;
		v.clear();
		idx.clear();
		for (int i = 0; i < n; i++) {
			cin >> s;
			v.push_back(s);
			idx.push_back(i);
		}

		long long c = 0;
		do {
			memset(tf, 0, sizeof tf);
			bool tff = true;
			string ttt = "";
			for (int i = 0; i < idx.size(); i++)
				ttt += v[idx[i]];
			// cout << ttt << endl;

			tf[ttt[0]] = 1;
			for (int i = 1; i < ttt.length(); i++) {
				if (ttt[i] != ttt[i-1]) {
					if (tf[ttt[i]])
						tff = false;
					else
						tf[ttt[i]] = 1;

					char chr = ttt[i];
					if (i < ttt.length() && ttt[i] == chr) {
						while (i < ttt.length() && ttt[i] == chr) {
							i++;
						}
						i--;
					}
				}
			}

			if (tff) {
				c++;
			}

		} while (next_permutation(idx.begin(), idx.end()));
		
		cout << c << endl;
	}

	return 0;
}