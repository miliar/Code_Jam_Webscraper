#include <stdio.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
using namespace std;
map<string, int> mp;
vector<int> c[20], a, b;
int n, m;
char str[100000];
char ss[20];
int u[10000];
int get() {
    if (mp.count(ss) == 0) {
        mp[ss] = m++;
    }
    return mp[ss];
}
void read(vector<int> &e) {
    e.clear();
    gets(str);
    int sn = 0;
    for (int i = 0; str[i]; i++) {
        if (str[i] == ' ') {
            ss[sn] = 0;
            e.push_back(get());
            sn = 0;
        } else {
            ss[sn++] = str[i];
        }
    }
    ss[sn] = 0;
    e.push_back(get());
}
int main(){
    int T, ri = 1, i, k;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        mp.clear();
        scanf("%d", &n);
        n -= 2;
        m = 0;
        gets(ss);
        read(a);
        read(b);
        for (i = 0; i < n; i++) read(c[i]);
        int ans = m;
        for (k = 0; k < (1<<n); k++) {
            for (i = 0; i < m; i++) u[i] = 0;
            for (i = 0; i < (int)a.size(); i++) u[a[i]] |= 1;
            for (i = 0; i < (int)b.size(); i++) u[b[i]] |= 2;
            for (i = 0; i < n; i++) {
                for (int j = 0; j < (int)c[i].size(); j++) {
                    if (k & (1<<i)) u[c[i][j]] |= 1;
                    else u[c[i][j]] |= 2;
                }
            }
            int cur = 0;
            for (i = 0; i < m; i++) {
                if (u[i] == 3) cur++;
            }
            if (cur < ans) ans = cur;
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
