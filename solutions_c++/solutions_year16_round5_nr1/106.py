#include <iostream>

using namespace std;

string S;

int main() {
	int tc;
	cin >> tc;
	
	for(int ti = 1; ti <= tc; ++ti) {
		cin >> S;
		
		int res = 0;
		while(true) {
			bool done = true;
			string X;
			for(int i = 0; i < (int)S.size();) {
				if(i + 1 < (int)S.size() && S[i] == S[i + 1]) {
					res += 10;
					i += 2;
					done = false;
				} else {
					X.push_back(S[i]);
					++i;
				}
			}
			swap(S, X);
			if(done) break;
		}
		
		res += 5 * (S.size() / 2);
		
		cout << "Case #" << ti << ": " << res << '\n';
	}
	
	return 0;
}
