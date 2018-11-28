#include<iostream>
#include<string>
#include<conio.h>

using namespace std;

string S[100];
int M[100]; //moves


bool AllAre(string s, char c) {
	bool same = true;
	for (unsigned i = 0; i < s.length(); i++)
		if (s[i] != c)
			same = false;

	return same;
}

void ReplaceAll(string &s, char c) {
	for (unsigned i = 0; i < s.length(); i++)
		s[i] = c;
}
int main() {	
	int T, i = 0;
	cin >> T;

	for (i = 0; i < T; i++)
		cin >> S[i];

	for (i = 0; i < T; i++) {
		string s = S[i];

		int count = 0;
		int n = s.size(), j = 0;

		if (AllAre(s, '+'))
			count = 0;
		else if (AllAre(s, '-'))
			count = 1;
		else {
			while (!AllAre(s, '+')) {
				if (AllAre(s, '-'))	{
					ReplaceAll(s, '+');
					count++;
				}
				else {
					for (j = 0; j < n; j++) {
						if ((s[j] == '+' && s[j + 1] == '-') || (s[j] == '-' && s[j + 1] == '+')) {
							for (int k = 0; k <= j; k++) {
								if (s[k] == '+') s[k] = '-';
								else if (s[k] == '-') s[k] = '+';
							}
							count++;
							break;
						}
					}
				}
			}
		}
		M[i] = count;
	}

	for (i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": " << M[i] << endl;
	}

	_getche();
	return 0;
}