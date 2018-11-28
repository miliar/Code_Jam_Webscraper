#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

const int MAXN = 110;
char laaaa[MAXN];
int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%s", laaaa);
        int len = strlen(laaaa), yuki = 0, hana = 0;
        while(yuki < len) {
            while(yuki < len && laaaa[yuki] == '+')
                yuki++;
            if(yuki < len) {
                while(yuki < len && laaaa[yuki] == '-')
                    yuki++;
                hana += 2;
            }
        }
        if(hana && laaaa[0] == '-') hana--;
        printf("Case #%d: %d\n", ++cas, hana);
    }
    return 0;
}
