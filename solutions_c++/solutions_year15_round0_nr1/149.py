#include <stdio.h>

int t, t0;

int sm;
char s[1010];

int main()
{
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        scanf("%d%s", &sm, s);
        int i, c, ans;
        for(i = 0, c = 0, ans = 0; i <= sm; i++){
            if(c < i){
                ans += i - c;
                c = i;
                }
            c += s[i] - '0';
            }
            printf("Case #%d: %d\n", t0 + 1, ans);
        }

    return 0;
}
