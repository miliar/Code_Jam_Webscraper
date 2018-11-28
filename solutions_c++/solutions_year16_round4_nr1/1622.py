#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, r, p, s, total;
char str[5000];

bool build(int n, int p, int r, int s) {
    if (p < 0 || r < 0 || s < 0) return false;
    //cout << n << ' ' << p << ' ' << r << ' ' << s << endl;
    if (n == 1) {
        str[0] = p ? 'P' : r ? 'R' : 'S';
        return true;
    }
    int x = n / 2 - r, y = n / 2 - s, z = n / 2 - p;
    if (!build(n / 2, y, z, x)) return false;
    for (int i = n / 2 - 1; i >= 0; --i) {
        if (str[i] == 'P') {
            str[i + i] = 'P';
            str[i + i + 1] = 'R';
        } else if (str[i] == 'R') {
            if (n == total) {
                str[i + i] = 'R';
                str[i + i + 1] = 'S';
            } else {
                str[i + i] = 'S';
                str[i + i + 1] = 'R';
            }
        } else {
            str[i + i] = 'P';
            str[i + i + 1] = 'S';
        }
    }
}

char a[5000], b[5000];
void minimize(int l, int r, char* str) {
    if (l == r) return;
    int m = (l + r) >> 1, sz = (r - l) >> 1;
    minimize(l, m, str);
    minimize(m + 1, r, str);
    memcpy(a, str, sizeof(char) * sz);
    memcpy(b, str + sz, sizeof(char) * sz);
    a[sz] = b[sz] = '\0';
    if (strcmp(a, b) > 0) {
        for (int i = 0; i < sz; ++i) str[l + i] = b[i];
        for (int i = 0; i < sz; ++i) str[m + i] = a[i];
    }
}

int main(){
	int T;
	cin >> T;
	for (int v = 0; v < T; ++v) {
		cout << "Case #" << v + 1 << ": ";
        cin >> n >> r >> p >> s;
        total = p + r + s;
        str[total] = '\0';
        if (!build(total, p, r, s)) cout << "IMPOSSIBLE" << endl;
        else {
            minimize(0, total, str);
            cout << str << endl;
        }
	}
}
