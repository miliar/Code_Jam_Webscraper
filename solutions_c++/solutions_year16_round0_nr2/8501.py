#include <bits/stdc++.h>

using namespace std;

int getn () {
	int n;
	scanf("%d", &n);
	return n;
}

int main () {
	int N = getn();

	for (int i=0; i<N; i++) {
		int count = 0;
		string s;
		cin >> s;
		char last = '.';
		for (int j=0; j<s.size(); j++) {
			//cout << ">" << s[j]  << "<" << endl;
			if (s[j] != last) count++;
			last = s[j];
		}
		count -= (s[s.size()-1] == '+');
		printf("Case #%d: %d\n", i+1, count);
	}
}