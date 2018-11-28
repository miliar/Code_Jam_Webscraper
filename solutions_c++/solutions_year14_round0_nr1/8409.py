#include <cstdio>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define MINX(a, b) ((a) < (b) ? (a) : (b));
#define MAX(a, b) ((a) > (b) ? (a) : (b));

typedef unsigned long long ulng;
typedef signed long long slng;
typedef unsigned int uint;
typedef signed int sint;

void solve()
{
	int f[4][4];
	int s[4][4];
	int a1, a2, r;
	cin >> a1;
	assert(a1 >= 1 && a1 <= 4);
	a1--;
	for (int j = 0; j < 4; j++) {
		cin >> f[j][0] >> f[j][1] >> f[j][2] >> f[j][3];
	}
	cin >> a2;
	assert(a2 >= 1 && a2 <= 4);
	a2--;
	for (int j = 0; j < 4; j++) {
		cin >> s[j][0] >> s[j][1] >> s[j][2] >> s[j][3];
	}
	r = -1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (f[a1][i] == s[a2][j]) {
				if (r >= 0) {
					cout << "Bad magician!";
					return;
				}
				r = f[a1][i];
			}	
		}
	}
	if (r >= 0)
		cout << r;
	else
		cout << "Volunteer cheated!";
}

int main()
{
	int c;
	cin >> c;
	for (int i = 1; i <= c; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
}
