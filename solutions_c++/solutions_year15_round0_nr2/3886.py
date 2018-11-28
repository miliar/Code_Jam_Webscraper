#include <fstream>
#include <iostream>

#include <string>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int T, D, p;
ifstream in("B-small-attempt8.in");
ofstream out("out.txt");

int find_max(string &s) {
	char max_val = '0';
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] > max_val) {
			max_val = s[i];
		}
	}
	return max_val;
}

int run_bfs(string &v) {

	sort(v.begin(), v.end());

	set<string> discovered;
	queue<pair<int,string>> q;
	q.push(make_pair(0, v));

	discovered.insert(v);

	while (!q.empty()) {

		int d = q.front().first;
		string s = q.front().second;
		q.pop();

		string tmp1;
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] - 1 > '0')
				tmp1.push_back(s[i]-1);
		}

		if (tmp1.length() > 0) {
			if (discovered.find(tmp1) == discovered.end()) {
				discovered.insert(tmp1);
				q.push(make_pair(d + 1, tmp1));
			}
		} else {
			return d + 1;
		}
		
		if (s.back() > '1') {
			for (char ch = s.back() - 1; ch >= '1'; ch--) {
				string tmp2 = s;
				char to_add = s.back() - ch + '0';
				tmp2.back() = ch;
				tmp2.push_back(to_add);

				sort(tmp2.begin(), tmp2.end());

				if (discovered.find(tmp2) == discovered.end()) {
					discovered.insert(tmp2);
					q.push(make_pair(d + 1, tmp2));
				}
			}
			
		}
	}

	return -1;
}

int main() {

	in >> T;
	for (int t = 1; t <= T; ++t) {
		in >> D;
		string s(D, ' ');
		for (int d = 0; d < D; ++d) {
			in >> p;
			s[d] = '0' + p;
		}

		out << "Case #" << t << ": " << run_bfs(s) << endl;

	}

	return 0;
}