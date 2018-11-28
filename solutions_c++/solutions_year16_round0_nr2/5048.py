//============================================================================
// Name        : ayman.cpp
// Author      : Ayman Mostafa
// Email       : ayman93live@hotmail.com
// Version     : v5.0
//============================================================================

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;

#define all(x) x.begin(),x.end()
#define allr(x) x.rbegin(),x.rend()
#define clr(v,d) memset(v,d,sizeof(v));

const double PI = 2 * acos(0.0);
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
void fastInOut();

long long power(long long x, long long y) {
	long long z = 1;
	for (long long i = 0; i < y; i++)
		z *= x;
	return z;
}
int comp_double(double a, double b) {
	if (fabs(a - b) <= 1e-10)
		return 0;
	return a < b ? -1 : 1;
}
bool ok(string s) {
	for (int i = 0; i < s.size(); i++)
		if (s[i] != '+')
			return false;
	return true;
}
char inverse(char x) {
	if (x == '-')
		return '+';
	return '-';
}
string rev(string s, int end) {
	for (int i = 0, k = end - 1; i < end && k >= 0; i++, k--) {
		char t = s[i];
		s[i] = s[k];
		s[k] = t;
	}
	return s;
}
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------

//##########################################################################################
//###################################MAIN FUNCTION##########################################
//##########################################################################################
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	//freopen("A-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	fastInOut();
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------
	int t;
	string s;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> s;
		int res = 0, point;
		while (true) {
			if (ok(s))
				break;
			res++;
			for (int i = 0; i < s.size(); i++)
				if (s[i] == '-')
					point = i;
			if (point == 0)
				break;
			char flag = s[0];
			bool diff = false;
			for (int i = 0; i < point; i++)
				if (s[i] != flag) {
					diff = true;
					break;
				}
			if (diff || flag == '-')
				s[point] = inverse(s[point]);
			for (int i = 0; i < point; i++)
				s[i] = inverse(s[i]);
			if (diff || flag == '-')
				s = rev(s, point);
			else
				s = rev(s, point - 1);
		}
		cout << "Case #" << i << ": " << res << endl;
	}
}
void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
