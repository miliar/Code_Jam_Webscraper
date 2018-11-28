#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char s[1024];
char ans[1024];
int main(){
    int ca;
    scanf("%d", &ca);
    for(int t=1;t<=ca;t++){
        scanf("%s", s);
        ans[0] = s[0];
        ans[1] = '\0';
        for(int i=1;s[i] != '\0';i++){
            char tmp1[1024];
            char tmp2[1024];
            strcpy(tmp1, ans);
            tmp1[i] = s[i];
            tmp1[i + 1] = '\0';
            strcpy(tmp2 + 1, ans);
            tmp2[0] = s[i];
            if(strcmp(tmp1, tmp2) > 0){
                strcpy(ans, tmp1);
            }else{
                strcpy(ans, tmp2);
            }
        }
        printf("Case #%d: %s\n", t, ans);
    }
    return 0;
}
