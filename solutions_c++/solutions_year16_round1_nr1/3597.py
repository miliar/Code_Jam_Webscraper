#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	for (int it = 0; it < t; ++it) {
		string s;
		cin >> s;
		int n = s.length();
		vector<char> a,b;
		b.push_back(s[0]);
		for (int i=1; i<n; ++i) {
			if (s[i] >= b.back()) {
				b.push_back(s[i]);
			} else {
				a.push_back(s[i]);
			}
		}
		cout << "Case #"<< (it+1) <<": ";
		for (int i = b.size() - 1; i>=0; --i) {
			cout << b[i];
		}
		for (int i=0; i< a.size(); ++i) {
			cout << a[i];
		}
		cout << endl;
		a.clear();
		b.clear();
	}
	return 0;
}