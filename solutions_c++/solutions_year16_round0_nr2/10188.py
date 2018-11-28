#include<stdio.h>

main(){
    freopen("B-large.in","r",stdin);
    freopen("Bout.out","w",stdout);
    int t,e,i,j;
    char S[250];
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%s",S);
        for(i=0,e=0;S[i+1]!=NULL;i++){
            if(S[i]!=S[i+1])
                e++;
        }
        if(S[i]=='-')
            e++;
        printf("Case #%d: %d\n",j,e);
    }
}
