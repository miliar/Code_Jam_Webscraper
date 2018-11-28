#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main(void) {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test_case;
	fin >> test_case;
	for (int test_idx = 1; test_idx <= test_case; test_idx++) {
		string s;
		fin >> s;

		set<string> all;
		queue<pair<string, int>> q;
		q.push(make_pair(string(1, s[0]), 0));
		while (!q.empty()) {
			string curr = q.front().first; 
			int idx = q.front().second; q.pop();
			if (idx == s.size() || all.find(curr) != all.end()) {
				continue;
			}

			all.insert(curr);
			q.push(make_pair(curr + s[idx + 1], idx + 1));
			q.push(make_pair(s[idx + 1] + curr, idx + 1));
		}

		cout << "Case #" << test_idx << ": " << *all.rbegin() << endl;
		fout << "Case #" << test_idx << ": " << *all.rbegin() << endl;
	}
	return 0;
}