#include <iostream>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

map<pair<char, char>, char> m; 
char mul(char a, char b) {
	char ans = m[make_pair(abs(a), abs(b))];
	if (a*b < 0)
		ans = -ans;
	return ans;
}
int main() {
	
	m[make_pair('i', 'j')] = 'k';
	m[make_pair('j', 'i')] = -'k';
	m[make_pair('j', 'k')] = 'i';
	m[make_pair('k', 'j')] = -'i';
	m[make_pair('k', 'i')] = 'j';
	m[make_pair('i', 'k')] = -'j';
	m[make_pair('i', 'i')] = -'1';
	m[make_pair('j', 'j')] = -'1';
	m[make_pair('k', 'k')] = -'1';
	m[make_pair('1', '1')] = '1';
	m[make_pair('1', 'i')] = 'i';
	m[make_pair('1', 'j')] = 'j';
	m[make_pair('1', 'k')] = 'k';
	m[make_pair('i', '1')] = 'i';
	m[make_pair('j', '1')] = 'j';
	m[make_pair('k', '1')] = 'k';
	
	int T; cin >> T;
	int t = 1;
	while (t <= T) {
		cout << "Case #" << t++ << ": ";
		
		int L, X; string s;
		cin >> L >> X >> s;
		string S;
		while (X--) {
			S += s;
		}
		int n = S.size();
		
		int i = 0, k = n-1;
		char first = '1', last = '1', middle = '1';
		
		while (i < k) {
			first = mul(first, S[i]);
			if (first == 'i') break;
			++i;
		}
		if (i >= k) {
			cout << "NO" << endl;
			continue;
		}
		
		while (i < k) {
			last = mul(S[k], last);
			if (last == 'k') break;
			--k;
		}
		if (i >= k) {
			cout << "NO" << endl;
			continue;
		}
		
		for (int j = i+1; j < k; ++j) {
			middle = mul(middle, S[j]);
		}
		if (middle == 'j') {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	
	}
	return 0;
}
