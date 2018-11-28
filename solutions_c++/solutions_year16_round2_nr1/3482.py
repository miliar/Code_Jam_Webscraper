//~In The Name Of Allah~//
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <sstream>
#include <fstream>
#include <functional>
#include <stack>
#include <utility> 
#include <set>
#include <list>
#include <queue>
#include <bitset>
#include <time.h>
using namespace std;

#define read freopen("in.txt", "r", stdin)
#define write freopen("out.txt", "w", stdout)
#define all(_) _.begin(), _.end()
#define rall(_) _.rbegin(), _.rend()
#define rep(i, j) for (int i = 0; i < j; i++)
#define Rep(i, j, k) for (int i = j; i < k; i++)
#define siz(_) (int)_.size()
#define ll long long
#define endl '\n'

const double PI = 2.0 * acos(0.0);
const double EX = 2.7182818284;
const int MOD = 1e9 + 7;
const int oo = 2e9 + 1e8;

ll gcd(ll x, ll y) { return !y ? x : gcd(y, x%y); }

string s[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
string ans;
bool done;

void solve(int have[], string tmp) {
	if (done)
		return;
	bool ret = 0;
	rep(i, 26)
		ret |= (have[i] != 0);
	if (!ret) {
		ans = tmp;
		done = 1;
		return;
	}
	rep(i, 10) {
		bool good = 1;
		rep(j, siz(s[i]))
			good &= (have[s[i][j] - 'A'] != 0);
		if (good) {
			tmp.push_back(i + '0');
			rep(j, siz(s[i]))
				have[s[i][j] - 'A']--;
			solve(have, tmp);
			tmp.pop_back();
			rep(j, siz(s[i]))
				have[s[i][j] - 'A']++;
		}
	}
	return;
}

int main() {
	read;
	write;
	int t;
	string str;
	cin >> t;
	Rep(q, 1, t + 1) {
		cin >> str;
		int have[26] = {};
		rep(i, siz(str))
			have[str[i] - 'A']++;
		solve(have, "");
		sort(all(ans));
		cout << "Case #" << q << ": " << ans << endl;
		done = 0;
	}
	return 0;
}