#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 200500;

char buf[N];

char st[N];
int spt = 0;

void solve(int cs) {
    scanf("%s", buf);
    int n = strlen(buf);
    int ans = 0;
    spt = 0;
    for (int i = 0; i < n; i++) {
        if (spt == 0) {
            st[spt++] = buf[i];
        } else {
            if (buf[i] == st[spt - 1])
                --spt, ans += 10;
            else
                st[spt++] = buf[i];
        }
    }
    assert(spt % 2 == 0);
    ans += spt / 2 * 5;
    printf("Case #%d: %d\n", cs, ans);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
}
