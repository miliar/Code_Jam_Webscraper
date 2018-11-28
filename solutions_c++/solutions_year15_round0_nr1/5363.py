#include <cstdio>
char s[2000];
int main(){
    freopen ("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase = 1; kase <= T; ++kase){
        int len;
        scanf("%d", &len);
        scanf("%s", s);
        int sum = s[0]-'0', ans = 0;
        for(int i = 1; i <= len; ++i) if(s[i] != '0'){
            if(sum < i) ans += i-sum, sum = i+s[i]-'0';
            else sum += s[i]-'0';
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    fclose(stdout);
    return 0;
}