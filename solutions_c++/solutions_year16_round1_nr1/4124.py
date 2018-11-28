#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

char str[1010];
char ans[2010];
int main() {
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%s", str);
        int len = strlen(str);
        int st = 1000, ed = 1000;
        ans[1000] = str[0];
        for(int i = 1; i < len; i++) {
            if(str[i] >= ans[st]) {
                st--;
                ans[st] = str[i];
            } else {
                ed++;
                ans[ed] = str[i];
            }
        }
        printf("Case #%d: ", ++cas);
        for(int i = st; i <= ed; i++)
            putchar(ans[i]);
        puts("");
    }
    return 0;
}
