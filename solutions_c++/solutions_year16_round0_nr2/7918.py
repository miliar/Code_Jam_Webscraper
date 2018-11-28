#include <iostream>
#include <string>
using namespace std;

string s;

int lastBlank() {
	int len = s.length();
	for(int i = len - 1; i >= 0; i--)
		if(s[i] == '-')
			return i;
	return -1;
}

void flip(int n) {
	for(int i = 0; i < n / 2; i++) {
		char aux = s[i];
		s[i] = s[n - 1 - i];
		s[n - 1 - i] = aux;
	}
	for(int i = 0; i < n; i++)
		s[i] = (s[i] == '-') ? '+' : '-';
}

int lastHappyBeforeBlank() {
	int len = s.length();
	if(s[0] == '-') return -1;
	for(int i = 1; i < len; i++) {
		if(s[i] == '-')
			return i - 1;
	}
	return len - 1;
}

int main() { 

	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> s;
		int l = s.length();
		int flips = 0;
		int len = s.length();
		while(lastBlank() >= 0) {
			if(s[0] == '-') 
				flip(lastBlank() + 1);
			else
				flip(lastHappyBeforeBlank() + 1);
			flips++;
		}
		cout << "Case #" << i + 1 << ": " << flips << endl;
	}
	return 0;
}
