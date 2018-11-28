#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef long long ll;

map<string,int> mp;

char s[22][20010];
vector<int> vt[22];
int is[22222], is2[22222];

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int t, cas = 1;
    int n;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        getchar();
        mp.clear();
        int tot = 0;
        for(int i = 1;i <= n; i++) {
            vt[i].clear();
            gets(s[i]);
            for(int j = 0;s[i][j]; j++) if(s[i][j] != ' ') {
                string cur = "";
                while(s[i][j] && s[i][j] != ' ') {
                    cur += s[i][j];
                    j++;
                }
                j--;
                if(!mp[cur]) mp[cur] = ++tot;
                vt[i].push_back(mp[cur]);
            }
        }
        memset(is, 0, sizeof(is));
        int add = 0;
        for(int i = 1;i <= 2; i++) {
            for(int k = 0;k < vt[i].size(); k++) {
                if(!is[vt[i][k]]) {
                    is[vt[i][k]] = i;
                } else if(is[vt[i][k]] != 3 && is[vt[i][k]] != i) {
                    is[vt[i][k]] = 3;
                    add++;
                }
            }
        }
        int full = (1<<n-2)-1;
        int ans = 1<<30;
        for(int i = 0;i <= full; i++) {
            for(int j = 1;j <= tot; j++) is2[j] = 0;
            int cur = 0;
            for(int j = 3;j <= n; j++) {
                int be;
                if(i>>(j-3)&1) be = 1;
                else    be = 2;
                for(int k = 0;k < vt[j].size(); k++) {
                    int a1 = is[vt[j][k]], a2 = is2[vt[j][k]];
                    if(!a1) {
                        if(!a2) {
                            is2[vt[j][k]] = be;
                        } else if(a2 != 3 && a2 != be) {
                            is2[vt[j][k]] = 3;
                            cur++;
                        }
                    } else {
                        if(a1 == 3 || a2 == 3) continue;
                        if(a1 != be) {
                            is2[vt[j][k]] = 3;
                            cur++;
                        }
                    }
                }
            }
            ans = min(ans, cur+add);
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
