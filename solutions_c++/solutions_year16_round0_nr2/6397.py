#include<cstdio>
#include<cstring>

char s[110];

int solve(int len, char sign);

int main(){
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%s", s);
        int len = strlen(s);
        printf("Case #%d: %d\n", ++cnt, solve(len, '+'));
    }
    return 0;
}

int solve(int len, char sign){
    if(len == 0) return 0;
    while(s[len-1] == sign && len > 0) len--;
    if(len == 0) return 0;

    char tar = (sign == '+') ? '-' : '+';
    return solve(len-1, tar) + 1;
}
