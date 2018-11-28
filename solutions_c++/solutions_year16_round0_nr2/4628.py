#include <bitset>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char p[128];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", p);
        int len = strlen(p);
        bitset<128> b;
        b.reset();
        for (int i = 0; i < len; ++i) {
            if (p[i] == '+') {
                b[i] = 1;
            }
        }
        int ans = 0, l = len - 1;
        while (b.count() < len) {
            // cout<<b<<endl;
            while (b[l]) {
                --l;
            }
            if (b[0]) {
                int a = l;
                while (b[a] == 0) {
                    --a;
                }
                for (int i = 0; i <= a; ++i) {
                    b.flip(i);
                }
                bitset<128> tmp = b;
                for (int i = 0; i <= a; ++i) {
                    b[i] = tmp[a - i];
                }
            } else {
                for (int i = 0; i <= l; ++i) {
                    b.flip(i);
                }
                bitset<128> tmp = b;
                for (int i = 0; i <= l; ++i) {
                    b[i] = tmp[l - i];
                }
            }
            ++ans;
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}