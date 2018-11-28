#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <complex>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

const int ONE = 1, I = 2, J = 3, K = 4;
int m[5][5];
const int N = 20000;
int pref[N], suff[N];

int value(char ch)
{
	if (ch == 'i') return I;
	if (ch == 'j') return J;
	if (ch == 'k') return K;
	cout << "WTF";
	return -1;
}

int mult(int left, int right)
{
	bool minus = (left < 0) ^ (right < 0);
	return (minus ? -1 : 1) * m[abs(left)][abs(right)];
}

int main()
{
//#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//#endif 
	m[ONE][ONE] = ONE; m[ONE][I] = I;    m[ONE][J]  = J;    m[ONE][K] = K;
	m[I][ONE]   = I;   m[I][I]   = -ONE; m[I][J]    = K;    m[I][K]   = -J;
	m[J][ONE]   = J;   m[J][I]   = -K;   m[J][J]    = -ONE; m[J][K]   = I;
	m[K][ONE]   = K;   m[K][I]   = J;    m[K][J]    = -I;   m[K][K]   = -ONE;

	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n, x; string s, p; cin >> n >> x >> p;
		n *= x;
		for (int i = 0; i < x; i++) s += p;
		for (int i = 0; i < n; i++)
		{
			pref[i] = value(s[i]); if (i > 0) pref[i] = mult(pref[i - 1], pref[i]);
			suff[n - 1 - i] = value(s[n - 1 - i]); if (n - i < n) suff[n - 1 - i] = mult(suff[n - 1 - i], suff[n - i]);
		}
		bool can = false;
		for (int i = 0; i + 2 < n; i++)
		{
			int center = value(s[i + 1]);
			for (int j = i + 2; j < n; j++)
			{
				can |= pref[i] == I && center == J && suff[j] == K;
				center = mult(center, value(s[j]));
			}
		}
		cout << "Case #" << t + 1 << ": " << (can ? "YES" : "NO") << endl;
	}
}