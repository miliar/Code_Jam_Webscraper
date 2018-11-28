#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int NMAX = 100000 + 7;
const int INF = 1000000000;

string shift(string s, int n) {
	for (int i=0;i<n-i-1;i++) {
		swap(s[i],s[n-i-1]);
	}
	for (int i=0;i<n;i++) {
		s[i] = '+' + '-' - s[i];
	}
	return s;
}


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	string s;

	cin >> t;
	for (int testNumber = 1; testNumber <= t; testNumber++) {
		cin >> s;
		cout << "Case #" << testNumber << ": ";
		int cur = 0;
		int lastPlus = 0;
		for (int i=s.length()-1;i>=0;i--) {
			if (s[i] != '+') {
				lastPlus = i + 1;
				break;
			}
		}
		int ans = 0;
		while (cur < lastPlus) {
			int i;
			for (i=cur; i<lastPlus;i++){
				if (s[i]!=s[cur]) {
					break;
				}
			}
			cur = i;
			ans ++;
		}
		cout << ans << endl;
	}
	return 0;
}