#include <iostream>
#include<stdio.h>
#include <string>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	//int n; scanf("%d", &n);
	int n; std::cin >> n;
	string output;
	for (int i = 1; i < n+1;i++) {
		string s; int k;
		cin >> s >> k;
		int ct = 0;
		int po = 0;
		while (((int)s.size() > k)) {
		
			if (s[0]=='-') {
				for (int j = 0; j < k;j++) {
					if (s[j] == '-') {
						s[j] = '+';
					}
					else {
						s[j] = '-';
					}
				}
				ct += 1;
			}
			s = s.substr(1,s.size()-1);
		}
		if (s == string(k, '+')) {
			output = "Case #" + to_string(i) + ": " + to_string(ct);
		}
		else if (s == string(k, '-')) {
			ct += 1;
			output = "Case #" + to_string(i) + ": " + to_string(ct);
		}
		else {
			output = "Case #" + to_string(i) + ": IMPOSSIBLE";
		}
		cout << output << endl;
	}
}