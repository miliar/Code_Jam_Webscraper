#include <stdio.h>

int main()
{
    int t,j=0;
    scanf("%d",&t);
    while(j<t)
    {
        int n,cnt=0,ans=0,i;
        char input[1001];
        scanf("%d %s",&n,input);
        cnt+=input[0]-48;
        //printf("n : %d ",n);
        for (i=1;i<=n;i++)
        {
            if (cnt<i&&input[i]!=48) {ans+=i-cnt;cnt+=ans;}
            cnt+=input[i]-48;
            //printf("ans : %d cnt : %d\n",ans,cnt);
        }
        j++;
        printf("Case #%d: %d\n",j,ans);
    }
}
