#include <stdio.h>
#include <string.h>

#define MAX 1123

int main(void){
    int t, caso = 1;
    char s[MAX], ans[MAX], a[MAX], b[MAX];

    scanf("%d", &t);
    while(t--){
        scanf("\n%s", s);
        for(int i = 0; i < strlen(s); i++){
            if(!i){ ans[i] = s[i]; }
            else{
                if(s[i] < ans[0])  ans[strlen(ans)] = s[i];
                else{
                    for(int j = strlen(ans); j > 0; j--) ans[j] = ans[j-1];
                    ans[0] = s[i];
                }
            }
            ans[i+1] = '\0';
        }
        printf("Case #%d: %s\n", caso++, ans);
    }

    return 0;
}
