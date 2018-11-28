#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
int t, n;
string s;
int c[1111];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cin >> n;
		memset(c, 0, sizeof(c));
		cin >> s;
		for(int i = 0; i <= n; ++i) {
			c[i] = s[i] - '0';
		}
		int add = 0, accum = 0;
		for(int i = 0; i <= n; ++i) {
			if (accum < i) {
				add += i - accum;
				accum = i;
			}
			accum += c[i];
		}
		cout << "Case #" << tc << ": " << add << endl;
	}
}
