#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	
	for (int e = 0; e < T; e++) {
		string s;
		cin >> s;
		string answer = "";
		size_t count[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		count[0] = std::count(s.begin(), s.end(), 'Z');
		count[2] = std::count(s.begin(), s.end(), 'W');
		count[6] = std::count(s.begin(), s.end(), 'X');
		count[4] = std::count(s.begin(), s.end(), 'U');
		count[5] = std::count(s.begin(), s.end(), 'F') - count[4];
		count[7] = std::count(s.begin(), s.end(), 'V') - count[5];
		count[1] = std::count(s.begin(), s.end(), 'O') - count[2] - count[4] - count[0];
		count[8] = std::count(s.begin(), s.end(), 'G');
		count[9] = std::count(s.begin(), s.end(), 'I') - count[8] - count[5] - count[6];
		count[3] = std::count(s.begin(), s.end(), 'T') - count[2] - count[8];
		
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < count[i]; j++) {
				answer += i + '0';
			}
		}
		
		cout << "Case #" << e + 1 << ": " << answer << endl;
	}
	
	return 0;
}

//"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
