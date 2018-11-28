#include <cstdio>
#include <cstring>

int T;

char s[105];

void solve(){
    scanf("%s", s);
    bool flag = 0;
    int len = strlen(s);
    int ans = 0;
    for (int i = 0; i < len; i++){
        if (flag == 0 && s[i] == '-'){
            flag = 1;
            ans += (i == 0 ? 1 : 2);
        }else if (flag == 1 && s[i] == '+'){
            flag = 0;
        }
    }
    printf("%d\n", ans);
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
