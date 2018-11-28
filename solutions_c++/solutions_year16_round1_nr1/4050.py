#include <iostream>
#include <string>

using namespace std;

int main() {

	int T;

	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;
		
		string solution = S;
		int a = 0;
		int b = S.size()-1;
		
		for (int i = S.size()-1 ; i >= 0; i--) {
			char c = S[i];
			int j = 0;
			
			for (j = 0; j < i; j++) {
				if (S[j] > c) {
					solution[b] = c;
					b--;
					break;
				}
			}
			
			if (j == i) {
				solution[a] = c;
				a++;
			}
		}
		
		cout << "Case #" << t << ": " << solution << '\n';
	}
}
