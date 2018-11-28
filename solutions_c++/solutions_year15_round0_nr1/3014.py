#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

char peo[1000];
int main() {
    freopen("A-large.in.txt", "r", stdin);
    freopen("aa.out", "w", stdout);
    int T; scanf("%d", &T);
    int cas = 0;
    while (T--) {
        int n; scanf("%d", &n);
        int stand = 0, invite = 0;
        scanf("%s", peo);
        for (int i=0; i<=n; ++i) {
            if (stand >= i) stand += peo[i]-'0';
            else {
                int t = i - stand;
                invite += t;
                stand += t + peo[i] - '0';
            }
        }
        printf("Case #%d: %d\n", ++cas, invite);
    }
    return 0;
}
