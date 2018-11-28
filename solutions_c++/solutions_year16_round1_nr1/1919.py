#include<cstdio>

int main(){
    freopen("input.in","r",stdin);
    freopen("pA_output.txt","w",stdout);
    
    int T;
    char s[1005], ans[2005];
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
        printf("Case #%d: ",cases);
        scanf("%s",s);
        int st=1000, ed=1000;
        ans[st]=s[0];
        for(int i=1; s[i]!='\0'; i++){
            if(s[i]>=ans[st]){
                ans[--st]=s[i];
            }
            else ans[++ed]=s[i];
        }
        for(int i=st; i<=ed; i++) printf("%c",ans[i]);
        printf("\n");
    }
    return 0;
}
