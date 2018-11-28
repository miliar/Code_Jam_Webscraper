#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cmath>

#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <iostream>
#include<fstream>

using namespace std;

#define rep(i, n) for (i = 0; i < (int)(n); i++)
#define repab(i, a, b) for (i = (int)(a); i <= (int)(b); i++)
#define repset(iter, a) for (__typeof((a).begin()) iter = (a).begin(); iter != (a).end(); iter++)
#define zero(a) memset(a, 0, sizeof(a))
#define all(a) (a).begin(), (a).end()
#define max(a,b) ((a)>(b)? (a):(b))
#define min(a,b) ((a)<(b)? (a):(b))

typedef long long ll;
typedef vector <int> vi;
/*
ll gcd(ll x, ll y) {
	ll ans = min(x, y);
	x = max(x, y);
	while (x%ans) {
		y = ans;
		ans = x%ans;
		x = y;
	}
	return ans;
}
*/
/*
void nextCombination(int n, int r, int*c) {
	if (c[0] == n - r) {//exit
		c[0] = -1;
		return;
	}
	for (int i = 1; i <= r; i++) {//increment
		if (c[r - i] < (n - i)) {
			c[r - i]++;
			for (i--; i; i--)c[r - i] = c[r - (i + 1)] + 1;
			return;
		}
	}
}
*/
int main()
{
	//freopen("s.in", "r", stdin);
	//freopen("s.out", "w", stdout);
	ifstream cin("l.in");
	ofstream cout("l.out");
	//ofstream cerr("err.out");
	int t, T;
	int i, j, k;
	cin >> T;
	string s, s1;
	repab(t, 1, T) {
		cin >> s;
		s1 = "";
		int len = s.length();
		char ch = s[0];
		rep(i, len) {
			if (s[i] >= ch) {
				ch = s[i];
				s1.insert(0, 1, ch);
			}
			else s1 += s[i];
		}
		cout << "Case #" << t << ": "<<s1<<endl;
		//printf("Case #%d: %d\n", t, ans);
	}
	system("pause");
	return 0;
}