#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
	int T;
	char S[1001];
	char out[2002];
	char* sp;
	char* word;
	char* last;
	char ch;

	cin >> T;
	for(int t=0; t<T; t++) {
		cin >> S;
		word = last = out + 1000;
		sp = S;
		*word = *sp;
		for(++sp; *sp != '\0'; ++sp) {
			if(*sp < *word) {
				++last;
				*last = *sp;
			} else {
				--word;
				*word = *sp;
			}
		}

		++last;
		*last = '\0';
		cout << "Case #" << (t+1) << ": " << word << endl;
	}

	return 0;
}
