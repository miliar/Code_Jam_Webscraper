#include <cstdio>

int T;
int k, c, s;

void solve(){
    scanf("%d%d%d", &k, &c, &s);
    if (k == 1) printf("1\n");
    else if (c == 1) for (int i = 1; i <= k; i++) printf("%d%c", i, i == k ? '\n' : ' ');
    else for (int i = 1; i <= k; i++) printf("%d%c", i + 1, i == k ? '\n' : ' ');
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
