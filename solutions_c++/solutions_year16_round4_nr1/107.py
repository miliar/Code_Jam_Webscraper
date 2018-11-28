#pragma warning(disable:4996)

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <random>
#include <time.h>
#include <tuple>
#include <functional>
#include <list>
#include <limits.h>
#define mp make_pair
#define ni(x) scanf("%d", &(x))
#define nii(x,y) scanf("%d%d",&(x),&(y))
#define mul(x,y) ((ll)(x)*(y)%mod)
#define mtp make_tuple
#define add(x,y) ((ll)(x)+(y))%mod
#define F(i,n) for(int i = 0; i < n; i++)
#define FF(i,n) for(int i = 1; i <= n; i++)

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const int mod = 1000000007;
const int inf = 2012345678;
const double pi = 3.1415926535897932384626433832795;
//----------------------------------------------------------------------------//

string solve(int x, int y, int z) {
	if (x + y + z == 1) {
		if (x == 1) return string("R");
		else if (y == 1) return string("S");
		else if (z == 1) return string("P");
	}
	int a = (x + y - z) / 2;
	int b = (y + z - x) / 2;
	int c = (x + z - y) / 2;
	if (a < 0 || b < 0 || c < 0) return string("IMPOSSIBLE");
	string s = solve(a, b, c);
	if (s == string("IMPOSSIBLE")) return s;
	string ret;
	for (auto &x : s) {
		if (x == 'R')ret.append(string("RS"));
		else if (x == 'S') ret.append(string("SP"));
		else ret.append(string("RP"));
	}
	return ret;
}
void srt(string& s) {
	if (s.size() == 1) return;
	string s1 = s.substr(0, s.size() / 2);
	string s2 = s.substr(s.size() / 2);
	srt(s1); srt(s2);
	if (s1 < s2) s = s1 + s2;
	else s = s2 + s1;
}

int main() {
#ifndef __GNUG__
	freopen("A-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; ni(T);
	while (T--) {
		static int casen = 0;
		printf("Case #%d: ", ++casen);

		int n; ni(n);
		int x, y, z; nii(x, y); ni(z);
		swap(y, z);
		string s = solve(x, y, z);
		if(s!= string("IMPOSSIBLE"))srt(s);
		printf("%s\n", s.c_str());
	}

	return 0;
}
