#include <iostream>
#include <string>
#include <bitset>
#include <algorithm>
using namespace std;

int answer(string &s) {
	bool done = false;
        int moves = 0;

	if(count(s.begin(), s.end(), '+') == s.length()) {
		return moves;
	}
	if(count(s.begin(), s.end(), '-') == s.length()) {
		return moves+1;
	}

        while(!done) {
                char curr = s[0];
		int rev_range = 0;
                moves++;

                for(int i = 1; i < s.length(); i++) {
                        if(s[i] != curr) {
                                rev_range = i-1;
				break;
                        }
                }
                if(curr == '-') {
                        for(int i = 0; i <= rev_range; i++) {
                                s[i] = '+';
                        }
                }
                else {
                        for(int i = 0; i <= rev_range; i++) {
                                s[i] = '-';
                        }
                }
                if(count(s.begin(), s.end(), '+') == s.length()) {
                        done = true;
                }
		if(count(s.begin(), s.end(), '-') == s.length()) {
			done = true;
			moves+=1;
		}
        }
        return moves;
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	string pattern;

	for(int i = 1; i <= t; i++) {
		cin >> pattern;
		cout << "Case #" << i << ": " << answer(pattern) << endl;
	}


	return 0;
}
