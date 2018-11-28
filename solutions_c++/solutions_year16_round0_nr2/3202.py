#include<stdio.h>
#include<string.h>
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,m,test,tt,i;
    char s[105];
    scanf("%d",&tt);
    for(test=0;test<tt;test++){
        scanf("%s",s);
        m=strlen(s);
        n=1;
        for(i=1;i<m;i++)
            if(s[i]!=s[n-1])    s[n++]=s[i];
        printf("Case #%d: %d\n",test+1,n-1+((s[n-1]-'-')?0:1));
    }
    return 0;
}
