#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long ll;
#define pair(x, y) make_pair(x, y)

#define N 100
int T, n, m, a[N + 1][N + 1];
int tc = 0;
bool v[N + 1][N + 1], r[N + 1], c[N + 1];

int main() {
freopen("1.in", "r", stdin);
freopen("1.out", "w", stdout);

cin >> T;
while (T--) {
cin >> n >> m;
for (int i = 1; i <= n; ++i)
for (int j = 1; j <= m; ++j)
cin >> a[i][j];

bool ok = true;
for (int w = 2; ok && w > 0; --w) {
for (int i = 1; i <= n; ++i)
for (int j = 1; j <= m; ++j)
if (a[i][j] <= w) v[i][j] = true;
else v[i][j] = false;
memset(r, 0, sizeof r), memset(c, 0, sizeof c);
for (int i = 1; i <= n; ++i) {
bool fine = true;
for (int j = 1; fine && j <= m; ++j)
if (!v[i][j]) fine = false;
r[i] = fine;
}
for (int i = 1; i <= m; ++i) {
bool fine = true;
for (int j = 1; fine && j <= n; ++j)
if (!v[j][i]) fine = false;
c[i] = fine;
}

for (int i = 1; ok && i <= n; ++i)
for (int j = 1; ok && j <= m; ++j) {
if (v[i][j] && !r[i] && !c[j]) ok = false;
if (!v[i][j] && (r[i] || c[j])) ok = false;
}
}
cout << "Case #" << ++tc << ": " << (ok ? "YES" : "NO") << endl;
}

return 0;
}


