#include <bits/stdc++.h>

using namespace std;

const int ONE = 0;
const int I = 1;
const int J = 2;
const int K = 3;
const int MINUS_ONE = 4;
const int MINUS_I = 5;
const int MINUS_J = 6;
const int MINUS_K = 7;

map<char, int> getElem;

int mulTable[4][4] = {
    {ONE, I, J, K},
    {I, MINUS_ONE, K, MINUS_J},
    {J, MINUS_K, MINUS_ONE, I},
    {K, J, MINUS_I, MINUS_ONE}
};


inline int mul(int a, int b)
{
    bool isMinusRes = (a >= 4) ^ (b >= 4);
    int r = mulTable[a % 4][b % 4];
    return (r + (isMinusRes ? 4 : 0)) % 8;
}

inline int divide(int c, int a)
{
    for (int b = 0; b < 8; b++) {
	if (mul(a, b) == c) {
	    return b;
	}
    }
    exit(777);
}

string s;
string res = "";
vector< int > pref;

void solve(int testnum)
{
    int l, x;
    cin >> l >> x;
    cin >> s;
    {
	res = "";
	for (int i = 0; i < x; i++) {
	    res = res + s;
	}
	s = res;
    }

    pref.resize(x * l);
    pref[0] = getElem[s[0]];
    for (int i = 0; i < l * x; i++) {
	pref[i] = mul(pref[i-1], getElem[s[i]]);
    }

    for (int q = 0; q <= l * x - 3; q++) {
	if (pref[q] != I) {
	    continue;
	}
	for (int w = q + 1; w <= l * x - 2; w++) {
	    if (divide(pref[w], pref[q]) != J) {
		continue;
	    }

	    if (divide(pref[l * x - 1], pref[w]) != K) {
		continue;
	    }

	    cout << "Case #" << testnum + 1 << ": YES\n";
	    return;
	}
    }

    cout << "Case #" << testnum + 1 << ": NO\n";
}

int main()
{
    getElem['i'] = I;
    getElem['j'] = J;
    getElem['k'] = K;
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int q = 0; q < t; q++) {
	solve(q);
    }
}
