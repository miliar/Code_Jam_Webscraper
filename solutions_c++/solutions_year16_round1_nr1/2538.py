#include <fstream>
#include <list>
#include <algorithm>
#include <string>
#include <deque>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

string process(string s) {
	deque<char> a;
	for (auto c : s) {
		if (!a.empty() && a.front() <= c) a.push_front(c);
		else a.push_back(c);
	}
	s.clear();
	s.insert(s.begin(), a.begin(), a.end());
	return s;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i != T; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i + 1 << ": " << process(s) << endl;
	}
	return 0;
}