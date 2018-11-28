#include "stdio.h"
#include "iostream"
#include "vector"
#include "queue"
#include "algorithm"
#include "deque"
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		cout << "Case #" << cs << ": ";
		string str;
		cin >> str;
		deque<char> ans;
		ans.push_back(str[0]);
		for (int i = 1; i < str.length(); i++) {
			auto ch = ans.begin();
			while (ch != ans.end() && *ch == str[i]) {
				ch ++;
			}
			if (ch==ans.end() || *ch < str[i]) {
				ans.push_front(str[i]);
			}
			else {
				ans.push_back(str[i]);
			}
		}
		for (auto i = ans.begin(); i != ans.end(); i++) {
			cout << *i;
		}
		cout << endl;
	}
	return 0;
}