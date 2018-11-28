#include <iostream>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <map>
#include <vector>
#include <string>
//#define endl '\n'
#pragma warning (disable : 4996)

using namespace std;

#define lli long long int
#define MP make_pair

const int N = (int)(1e5);
const int M = (int)(1e5 + 20);

int mul[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};

int multiply(int a, int b)
{
	int sign = 1;
	if (a < 0) { sign *= -1; a = -a; }
	if (b < 0) { sign *= -1; b = -b; }
	return sign * (mul[a][b]);
}

bool correctI[N], correctK[N];
char str[N];

int toInt(char c) {
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	return 4;
}

int main()
{
//#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//#endif
    int T;
	cin >> T;
	for(int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
	
		int l, x;
		cin >> l >> x;
		string s;
		cin >> s;
		int n = l*x;
		for(int i = 0; i < n; ++i) str[i] = s[i % l];

		int cur = 1;
		for(int i = 0; i < n; ++i) {
			cur = multiply(cur, toInt(str[i]));
			correctI[i] = (cur == 2);
		}
		cur = 1;
		for(int i = n-1; i >= 0; --i) {
			cur = multiply(toInt(str[i]), cur);
			correctK[i] = (cur == 4);
		}

		bool ok = false;

		for(int i = 1; i < n-1 && !ok; ++i) {
			if (!correctI[i-1]) continue;
			cur = 1;
			for(int j = i; j < n-1; ++j) {
				cur = multiply(cur, toInt(str[j]));	
				if (cur == 3 && correctK[j+1]) {
					ok = true;
					break;
				}
			}
		}

		cout << (ok ? "YES" : "NO");

		cout << endl;
	}
    return 0;
}