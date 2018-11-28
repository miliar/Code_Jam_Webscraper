#include <bits/stdc++.h>

using namespace std;

string solve(string s, int size) {
	if (s[0] == '-') {
		int last = size;
		while (s[last-1] == '+')
			last--;
		for (int i=0; i<last; i++) {
			if (s[i] == '+') s[i] = '-';
			else s[i] = '+';
		}
		reverse(s.begin(), s.begin()+last);
		return s;
	}
	else {
		int i=0; 
		while (s[i] == '+')
			i++;
		for (int j=0; j<i; j++)
			s[j] = '-';
		reverse(s.begin(), s.begin()+i);
		return s;
	}
}

bool happy(string s, int size) {
	for (int i=0; i<size; i++)
		if (s[i] == '-')
			return false;
	return true;
}

int main() {
	int test, size, count;
	string s;
	cin >> test;
	for (int tt=1; tt<=test; tt++) {
		cin >> s;
		size = s.size();
		count = 0;
		while (!happy(s, size)) {
			s = solve(s, size);
			size = s.size();
			count++;
		}
		printf("Case #%d: %d\n", tt, count);
	}
	return 0;
}