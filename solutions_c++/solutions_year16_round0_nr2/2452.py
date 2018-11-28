#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main() {
	ofstream ofs("out.txt");
	int t;	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;	cin >> s;
		ofs << "Case #" << i << ": ";
		bool cur = (s[0] == '+' ? true : false);
		int ret = 0;
		for (int i = 1; i < s.length(); i++) {
			bool next = (s[i] == '+' ? true : false);
			if (cur^next) {
				cur = next;
				ret++;
			}
		}
		if (!cur) ret++;
		ofs << ret << endl;
	}
	return 0;
}