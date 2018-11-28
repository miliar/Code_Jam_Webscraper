#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;
vector<vector<string> > words;
map<string, int> l[2];
int o;
int n;

void search(int index, int now) {
	if (o >= 0 && now >= o) return;
	if (index == n) {
/*		int now = 0;
		int j = 0;
//		for (int j = 0; j <= 1; j ++) 
			for (map<string, int>::iterator it = l[j].begin(); it != l[j].end(); it ++) {
				if (it -> second == 0) continue;
				string wd = it -> first;
				if (l[1 - j].find(wd) == l[1 - j].end()) continue;
				if (l[1 - j][wd] == 0) continue;
				now ++;
//				cout << wd << endl;
			}
//		now = now / 2;
*/
		if (o < 0 || now < o) {
			o = now;
		}
		return;
	}
	for (int j = 0; j <= 1; j ++) {
		int delta = 0;
		for (int i = 0; i < words[index].size(); i ++) {
			if (l[j].find(words[index][i]) == l[j].end() || l[j][words[index][i]] == 0) {
				l[j][words[index][i]] = 1;
				if (l[1 - j].find(words[index][i]) != l[1 - j].end() && l[1 - j][words[index][i]] != 0) delta ++;
			} else {
				l[j][words[index][i]] ++;
			}
		}
//		cout << "index " << index << " j " << j << " now + delta " << now + delta << endl;
		search(index + 1, now + delta);
		for (int i = 0; i < words[index].size(); i ++) {
			l[j][words[index][i]] --;
		}
	}
}

int main() {
	int testcases;
	cin >> testcases;
	for (int testcase = 0; testcase < testcases; testcase ++) {
		for (int j = 0; j <= 1; j ++) 
			l[j].clear();
		cin >> n;
		words.clear();
		words.resize(n);
		string line;
		getline(cin, line);
		for (int i = 0; i < n; i ++) {
			getline(cin, line);
			istringstream iss(line);
			string s;
			while (iss >> s) {
				words[i].push_back(s);
			}
		}

		int now = 0;

		for (int j = 0; j <= 1; j ++) {
			for (int i = 0; i < words[j].size(); i ++) {
				if (l[j].find(words[j][i]) == l[j].end()) {
					l[j][words[j][i]] = 1;
					if (l[1 - j].find(words[j][i]) != l[1 - j].end() && l[1 - j][words[j][i]] != 0) now ++;
				} else {
					l[j][words[j][i]] ++;
				}
			}
		}

		o = -1;
		search(2, now);

		cout << "Case #" << testcase + 1 << ": " << o << endl;
	}
	return 0;
}