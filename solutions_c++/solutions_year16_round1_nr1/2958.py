#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;


int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	bool first = true;
	for (int t = 1; t <= T; t++){
		if (first) first = false;
		else cout << endl;
		cout << "Case #" << t << ": ";
		
		string s;
		cin >> s;
		string ans;
		ans += s[0];
		for (int i = 1; i < s.length(); i++){
			if (s[i] >= ans[0]){
				ans = s[i] + ans;
			}
			else{
				ans += s[i];
			}
		}
		cout << ans;
	}
	exit(0);
}