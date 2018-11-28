#include <stdio.h>
char s[1005];
int main (void)
{
    int i,j,n,t,p,cnt;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&n);

    for(i=0;i<n;i++){
        scanf("%d",&t);
        scanf("%s",s);
        if(t==0){
            printf("Case #%d: 0\n",i+1);
            continue;
        }
        cnt=0;
        s[0]-='0';
        p=s[0];
        for(j=1;j<=t;j++){
            s[j]-='0';
            if(p+cnt<j)
                cnt=j-p;
            p+=s[j];
        }
        printf("Case #%d: %d\n",i+1,cnt);

    }

    return 0;
}
