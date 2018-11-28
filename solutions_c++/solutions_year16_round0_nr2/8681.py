#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
using namespace std;

string flip(string s, int x) {
	string ret = "";
	for (int i = x; i >= 0; i--) 
		ret += (s[i] == '-' ? '+' : '-');
	for (int i = x + 1; i < s.size(); i++)
		ret += s[i];
	return ret;
}

int main(void) {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test_case;
	fin >> test_case;
	for (int test_idx = 1; test_idx <= test_case; test_idx++) {
		string st;
		fin >> st;

		int n = st.size();

		map<string, int> d;
		queue<string> q;
		q.push(st);
		while (!q.empty()) {
			string curr = q.front(); q.pop();
			if (curr == string(n, '+')) break;

			for (int i = 0; i < n; i++) {
				string next = flip(curr, i);
				if (d[next] == 0 || d[curr] + 1 < d[next]) {
					q.push(next);
					d[next] = d[curr] + 1;
				}
			}
		}

		cout << "Case #" << test_idx << ": " << d[string(n, '+')] << endl;
		fout << "Case #" << test_idx << ": " << d[string(n, '+')] << endl;
	}

	return 0;
}