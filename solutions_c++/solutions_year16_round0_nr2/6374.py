#include<stdio.h>
#include<string.h>
char s[105];
int n[105];
int main(){
    int T, ca = 1;
    scanf("%d", &T);
    while(T--){
        scanf("%s", s);
        int len = strlen(s);
        for(int i = 1; i <= len; ++i) n[i] = s[i-1]=='+'? 0 : -1;
        int ans = 0, last = n[1];
        for(int i = 2; i <= len; ++i){
            if(n[i] != last){
                ans += 1;
                last = n[i];
            }
        }
        printf("Case #%d: %d\n", ca++, ans-n[len]);
    }
}
