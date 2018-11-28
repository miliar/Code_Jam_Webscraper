#include <bits/stdc++.h>

using namespace std;

int flip(int end, string &s) {
	string s_prev = s;
	for (int i = 0, j = end; i <= j; i++, j--) {
		char c = s[i] == '-' ? '+' : '-';
		s[i] = s[j] == '-' ? '+' : '-';
		s[j] = c;
	}
	return 1;
}

int main() {
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		string s;
		cin >> s;
		int answer = 0;
		int index = s.length() - 1;
		while (index >= 0) {
			if (s[index] == '+') {
				index--;
				continue;
			}
			else {
				if (s[0] == '-') {
					flip(index, s);
					answer++;
				}
				else {
					int index2 = index - 1;
					while (index2 >= 0 && s[index2] == '-') index2--;
					answer += flip(index2, s);
					answer++;
					flip(index, s);
				}
			}
			index--;
		}
		
		cout << "Case #" << i + 1 << ": " << answer;
		if (i != T - 1) cout << endl;
	}
	
	return 0;
} 
