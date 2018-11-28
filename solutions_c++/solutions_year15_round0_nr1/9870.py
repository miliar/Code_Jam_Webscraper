#include<stdio.h>

int main(){
    int t,smax,i,j;
    long count=0,ans=0;;
    char s[1003],ch;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%d",&smax);
        count=ans=0;
        scanf("%c",&ch);
        for(i=0;i<=smax;i++){
            scanf("%c",&s[i]);
            if((s[i]>'0')&& (count<i)){
                ans=ans +(i- count);
                count+=ans;
            }
            if(s[i]>'0')
                count+=s[i]-'0';
        }
        printf("Case #%d: %ld\n",j,ans);
    }
    return 0;
}
