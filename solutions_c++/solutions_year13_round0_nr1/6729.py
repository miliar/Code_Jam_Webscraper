#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

typedef long long ll;
#define pair(x, y) make_pair(x, y)
int T;
string s[4];

inline int row(int x) {
int cur = 0;
for (int i = 0; i < 4; ++i) {
if (s[x][i] == '.') return 0;
if (s[x][i] != 'T') {
if (!cur) cur = s[x][i];
else if (cur != s[x][i]) return -1;
}
}
return cur;
}

inline int column(int x) {
int cur = 0;
for (int i = 0; i < 4; ++i) {
if (s[i][x] == '.') return 0;
if (s[i][x] != 'T') {
if (!cur) cur = s[i][x];
else if (cur != s[i][x]) return -1;
}
}
return cur;
}

inline int diagonal(int x) {
int cur = 0;
if (x == 0) {
for (int i = 0; i < 4; ++i) {
if (s[i][i] == '.') return 0;
if (s[i][i] != 'T') {
if (!cur) cur = s[i][i];
else if (cur != s[i][i]) return -1;
}
}
} else {
for (int i = 0; i < 4; ++i) {
if (s[3 - i][i] == '.') return 0;
if (s[3 - i][i] != 'T') {
if (!cur) cur = s[3 - i][i];
else if (cur != s[3 - i][i]) return -1;
}
}
}
return cur;
}

int tc = 0;
string state;

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
cin >> T;
while (T--) {
for (int i = 0; i < 4; ++i) cin >> s[i];
int ans = INT_MIN;
for (int i = 0; i < 4; ++i) ans = max(ans, row(i));
for (int i = 0; i < 4; ++i) ans = max(ans, column(i));
ans = max(ans, diagonal(0));
ans = max(ans, diagonal(1));
if (ans == 0) state = "Game has not completed";
else if (ans == -1) state = "Draw";
else if (ans == 'X') state = "X won";
else state = "O won";
cout << "Case #" << ++tc << ": " << state << endl;
}

return 0;
}
