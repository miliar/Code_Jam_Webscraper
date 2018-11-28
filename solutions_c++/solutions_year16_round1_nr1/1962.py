#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		string S, res;
		cin >> S;
		char firstLetter = S[0];
		res = firstLetter;
		for( int j = 1; j < S.length(); j++) {
			if((int)(S[j]) >= (int)(firstLetter)) {
				firstLetter = S[j];
				res = S[j] + res;
			}
			else {
				res = res + S[j];
			}
		}
		cout << "Case #" << i << ": " << res << endl; 
	}
	
	return 0;
}
