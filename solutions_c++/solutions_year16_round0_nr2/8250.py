#include<stdio.h>
#include<string.h>

int main(){

    freopen("B-large.in", "r", stdin);
    freopen("file.txt", "w", stdout);

    int T, i, n, rs;
    char s[333];

    scanf("%d", &T);
    for(int cas = 0; cas < T; ++cas){
        scanf("%s", s);

        n = strlen(s);
        rs = 0;

        i = 0;
        if(s[i] == '-') rs = 1;
        while(i < n && s[i] == '-') i++;

        while(i < n){
            if(s[i] == '-'){
                while(i < n && s[i] == '-') i++;

                rs += 2;
            }else
                i++;
        }

        printf("Case #%d: %d\n", cas + 1, rs);

    }


return 0;
}
