#include <bits/stdc++.h>
const int N = 10010;

char s[N], _t[N * 3];

int main(){
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        scanf("%s", s);
        char *a = _t + N, *b = _t + N, pre = 0;
        for(int i = 0; s[i]; ++i){
            if(s[i] >= pre){
                *--a = s[i];
                pre = s[i];
            }
            else{
                *b++ = s[i];
            }
        }
        *b =0;
        printf("Case #%d: %s\n", cas, a);
    }
    return 0;
}