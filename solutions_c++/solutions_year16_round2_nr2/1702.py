#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define ld long double
#define endl "\n"


using namespace std;

bool cmp(string & s, string & c) {
	while(c.length() < s.length()) c.insert(0, 1, '0');
	for(int i = 0; i < s.length(); i++) {
		if(s[i] != '?' && s[i] != c[i]) return false;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(0);	

	int n;
	cin >> n;

	for(int test = 1; test <= n; test++) {
		cout << "Case #" << test << ": ";
		string str1, str2;
		cin >> str1 >> str2;
		int ndigits = max(str1.length(), str2.length());
		int MAX = 1;
		for(int i = 0; i < ndigits; i++) MAX *= 10;

		int bestDiff = numeric_limits<int>::max();
		string bestS1, bestS2;
		for(int s1 = 0; s1 < MAX; s1++) {
			string c1 = to_string(s1);
			if(!cmp(str1, c1)) continue;

			for(int s2 = 0; s2 < MAX; s2++) {
				string c2 = to_string(s2);
				if(cmp(str2, c2)) {
					int diff = abs(s1-s2);
					if(diff < bestDiff) {
						bestDiff = diff;
						bestS1 = c1;
						bestS2 = c2;
					}
				}

			}
		}

		cout << bestS1 << ' ' << bestS2 << endl;
	}

	return 0;
}
