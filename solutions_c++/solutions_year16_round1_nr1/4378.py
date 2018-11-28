#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,j;
	cin >> t;
	for (j = 0; j < t; j++) {
		int i,e,f;
		string s;
		cin >> s;
		list <char> l;
		l.push_back(s[0]);
		for (i = 1; i < s.length(); i++) {
			e = s[i] - '\0' - 64;
			f = l.front() - '\0' - 64;
			if (e >= f) {
				l.push_front(s[i]);
			}
			else {
				l.push_back(s[i]);
			}
		}
		cout << "Case #" << j+1 <<": ";
		for (list<char>::iterator it= l.begin(); it != l.end(); ++it)
		    cout << *it;
		   cout  << endl;

	}
	return 0;
}
