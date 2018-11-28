#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

char str[2010];
char ans[2010];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, ic = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%s", str);
        int len = strlen(str);
        int st = 1010, ed = 1010;
        ans[1010] = str[0];
        for(int i = 1; i < len; ++i) {
            if(str[i] >= ans[st]) {
                st--;
                ans[st] = str[i];
            } else {
                ed++;
                ans[ed] = str[i];
            }
        }
        printf("Case #%d: ", ic++);
        for(int i = st; i <= ed; ++i)
            putchar(ans[i]);
        puts("");
    }
    return 0;
}
