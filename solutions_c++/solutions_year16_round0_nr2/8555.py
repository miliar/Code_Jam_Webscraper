#include <bits/stdc++.h>
#define _ << " " <<

#define X first
#define Y second

using namespace std;

typedef pair<int, int> Point;
typedef long long lint;
typedef int8_t int8;

char p[200];
int len;
void solve() {
    scanf("%s", p); len = strlen(p);
    p[len] = '+';
    lint ans = 0;
    for(int i = 0; i < len; ++i) {
        ans += (p[i] != p[i+1]);
        if(p[i] == p[i+1]) continue;
    }
    cout << ans << endl;
}


int main() {
    int T; scanf("%d", &T);

    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

