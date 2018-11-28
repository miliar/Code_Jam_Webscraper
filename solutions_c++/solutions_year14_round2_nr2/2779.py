#include <stdio.h>
#include<string.h>
int main()
{
    freopen("/Users/rohansuri/Documents/coding/coding/B-small.in","r",stdin);
    //FILE *fp=freopen("/Users/rohansuri/Documents/coding/coding/IN.in","r",stdin);
    //if(fp==NULL)printf("yo");
    freopen("/Users/rohansuri/Documents/coding/coding/OUT.out","w",stdout);
    int T,t,ans,i,j,a,b,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {   ans=0;
        scanf("%d%d%d",&a,&b,&k);
        ans=a+b-1;//for all 0 checks
        for(i=1;i<a;i++)
            for(j=1;j<b;j++)
                if((i&j)<k)ans++;
        printf("Case #%d: %d\n",t,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}