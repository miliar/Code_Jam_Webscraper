#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		string answer = s.substr(0, 1);
		int len = s.length();
		for (int k = 1; k < len; ++k) {
			if (s[k] >= answer[0]) {
				answer = s.substr(k, 1) + answer;
			} else {
				answer = answer + s.substr(k, 1);
			}
		}
		cout << "Case #" << i+1 << ": ";
		cout << answer << endl;
	}
}
