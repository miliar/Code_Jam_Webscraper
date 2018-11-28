#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#define INF 2100000000
using namespace std;
char str[11111];
int a[11111];

int main(){
    int T, n, i, cas = 0;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--){
        scanf("%d", &n);
        scanf("%s", str);
        n++;
        memset(a, 0, sizeof(a));
        for(i = 0; i < n; i++)
            a[i] = str[i] - '0';
        int ans = 0, now = a[0];
        for(i = 1; i < n; i++){
            if (now < i) {
                ans += i - now;
                now = i;
            }
            now += a[i];
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
