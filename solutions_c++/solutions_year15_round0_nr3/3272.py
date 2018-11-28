#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

int L, X;
string a;
string s; int n;

int d[10000][10000];

const int O = 0, I = 1, J = 2, K = 3;
const int NO = 4, NI = 5, NJ = 6, NK = 7;
const int T[4][4] = {
	{O, I, J, K},
	{I, NO, K, NJ},
	{J, NK, NO, I},
	{K, J, NI, NO}
};
int init(char s) {
	if(s == 'i') return I;
	if(s == 'j') return J;
	if(s == 'k') return K;
	throw 1;
}

int mul(int x, int y) {
	int sgn = 1;
	if(x > 3) x -= 4, sgn *= -1;
	if(y > 3) y -= 4, sgn *= -1;

	int z = T[x][y];
	if(sgn == -1)  z = (z + 4) % 8;
	return z;
}

bool go()
{
	n = s.size();
	for(int i=0; i<n; ++i)
		d[i][i] = init(s[i]);
	for(int g=1; g<n; ++g) {
		for(int i=0; i<n-g; ++i) {
			int j = i + g;
			d[i][j] = mul(d[i][j - 1], d[j][j]);
		}
	}
	for(int i=1; i<n; ++i) {
		for(int j=i+1; j<n; ++j) {
			if(d[0][i-1] == I &&
			   d[i][j-1] == J &&
			   d[j][n-1] == K)
				return true;
		}
	}

	return false;
}

int main() {
	int T;
	cin >> T;
	for(int k=1; k<=T; ++k) {
		cin >> L >> X >> a;
		s = "";
		REP(k, X) s += a;
		printf("Case #%d: %s\n",
				k, go() ? "YES" : "NO");
	}
	return 0;
}

