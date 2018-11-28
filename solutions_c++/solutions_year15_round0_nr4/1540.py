#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(false); cin.tie(NULL);

typedef long long ll;

bool m[5][5][5];

int main() { _
	m[2][2][2] = true;
	m[1][3][2] = false;
	m[4][1][4] = false;
	m[2][3][3] = true;
	m[4][3][2] = true;
	m[3][3][4] = false;
	m[1][4][4] = false;
	m[4][1][3] = false;
	m[1][4][3] = false;
	m[1][4][1] = true;
	m[1][2][2] = true;
	m[3][1][3] = false;
	m[2][3][1] = true;
	m[2][3][4] = false;
	m[1][3][3] = false;
	m[3][3][3] = true;
	m[3][4][2] = true;
	m[3][4][1] = true;
	m[1][3][4] = false;
	m[1][4][2] = true;
	m[2][1][2] = true;
	m[2][4][2] = true;
	m[2][2][3] = false;
	m[2][3][2] = true;
	m[1][2][4] = false;
	m[2][1][4] = false;
	m[1][2][3] = false;
	m[4][2][2] = true;
	m[2][4][1] = true;
	m[3][1][4] = false;
	m[2][2][4] = false;
	m[1][1][1] = true;
	m[1][1][3] = false;
	m[4][2][1] = true;
	m[4][3][3] = true;
	m[2][4][4] = false;
	m[4][4][2] = true;
	m[4][1][1] = true;
	m[4][2][4] = false;
	m[3][3][2] = false;
	m[4][1][2] = true;
	m[1][1][4] = false;
	m[4][2][3] = false;
	m[4][4][3] = false;
	m[3][3][1] = true;
	m[3][4][4] = true;
	m[4][3][1] = true;
	m[3][1][1] = true;
	m[4][4][4] = true;
	m[3][1][2] = false;
	m[3][4][3] = true;
	m[2][1][1] = true;
	m[3][2][3] = true;
	m[4][3][4] = true;
	m[1][2][1] = true;
	m[3][2][1] = true;
	m[1][1][2] = false;
	m[2][2][1] = true;
	m[3][2][4] = false;
	m[4][4][1] = true;
	m[1][3][1] = true;
	m[2][4][3] = false;
	m[2][1][3] = false;
	m[3][2][2] = true;
	ll t;
	cin >> t;
	for (ll test = 1; test <= t; ++test) {
		cout << "Case #" << test << ": ";
		int x, r, c;
		cin >> x >> r >> c;
		cout << (m[r][c][x]? "GABRIEL": "RICHARD") << endl;
	}
}
