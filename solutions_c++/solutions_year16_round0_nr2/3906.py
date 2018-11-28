#include <stdio.h>
#include <string.h>

int main()
{
    int T, c, i, ans;
    char S[102];
    scanf("%d\n", &T);
    for(c=1; c<=T; c++){
        ans = 0;
        gets(S);
        i=0;
        while (i<strlen(S)){
            if(S[i] == '-'){
                ans += 1;
                while(S[i] == '-' && i <strlen(S)){
                    i++;
                }
            }
            if(S[i] == '+'){
                while (S[i] == '+' && i < strlen(S)){
                    i++;
                }
                if (i==strlen(S))
                    break;
                else if (S[i] == '-')
                    ans += 1;
            }
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
