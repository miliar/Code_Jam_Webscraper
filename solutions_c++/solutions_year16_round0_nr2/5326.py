#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++) {
		
		string s;
		cin >> s;
		
		int n = 0;
		
		while(!s.empty()) {
			
			while(s.back() == '+') {
				s.pop_back();
			}
			
			if (!s.empty() && s.front() == '-') {
				reverse(s.begin(), s.end());
				
				for(int i = 0; i < s.length(); i++)
					s[i] = s[i]=='+'? '-' : '+';
					
				++n;
			} else
			if (!s.empty() && s.front() == '+') {
				for(int i = 0; i < s.length(); i++) {
					if (s[i] == '+') {
						s[i] = '-';
					} else {
						break;
					}
				}
				++n;
			}
		}
		
		cout << "Case #" << t << ": " << n << endl;
	}
	
	return 0;
}