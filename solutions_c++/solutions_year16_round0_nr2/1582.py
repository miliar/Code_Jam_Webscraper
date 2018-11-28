#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
char ch[1100];
int main(){
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t; scanf("%d", &t);
    while (t--){
        int n;
        static int ca = 0;
        printf("Case #%d: ", ++ ca);
        scanf("%s", ch);
        n = strlen(ch);
        char state = ch[0];
        int now = 1, ans = 0;
        while (now < n){
            while (now < n && ch[now] == state) now++;
            if (now == n) break;
            ans ++;
            state = ch[now];
        }
        if (state == '-') ans++;
        printf("%d\n", ans);
    }
}
