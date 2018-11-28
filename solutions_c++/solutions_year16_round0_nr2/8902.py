#include <iostream>
#include <string>
using namespace std;

int counter = 1;

void print(int number) {
	cout << "Case #" << counter++ << ": " << number << endl;
}

bool contains(string s, char c) {
	for (int n = 0; n < s.length(); n++)
		if (s[n] == c)
			return true;
	return false;
}

int count = 1;

void doJob(string* S, int l) {
    for (int n = 0, count; n < l; n++) {
		count = 0;
		for (; contains(S[n], '-'); ) {
            if(S[n][0] == '+')
            {
                for (int m = 0; m < S[n].length(); m++){
                    if (S[n][m] == '+')
                        S[n][m] = '-';
                    else break;
                }
            } else {
                for (int m = 0; m < S[n].length(); m++){
                    if (S[n][m] == '-')
                        S[n][m] = '+';
                    else break;
                }
            }
            count++;
        }
        print(count);
    }
}

int main() {
	int T;
	cin >> T;
	string Ss[T];

	for (int t = 0; t < T; t++){
		cin >> Ss[t];
	}

	doJob(Ss, T);
	return 0;
}
