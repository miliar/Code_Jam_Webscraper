#include <bits/stdc++.h>
using namespace std;


char s[10005];

int CAS;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%s", s);
        printf("Case #%d: ", cas);
        int n = strlen(s);
        char last = '+';
        int ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] != last) {
                last = s[i];
                ans++;
            }
        }
        printf("%d\n", ans);
    }
}
