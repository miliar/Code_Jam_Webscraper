#include <cstdio>
#include <cstring>

int T;
char s[1005];
char out[10005];

void solve(){
    scanf("%s", s);
    memset(out, 0, sizeof(out));
    int start = 2000, last = 2000;
    int n = strlen(s);
    out[2000] = s[0];
    for (int i = 1; i < n; i++){
        if (s[i] >= out[start]){
            out[--start] = s[i];
        }else{
            out[++last] = s[i];
        }
    }
    printf("%s\n", out + start);
}

int main(){
    scanf("%d", &T);
    for (int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
