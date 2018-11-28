#include<bits/stdc++.h>
int main()
{
    int t,n,sum,frnd,x,i;
    char str[2000];
    scanf("%d",&t);
    for(x=1;x<=t;x++)
    {
        scanf("%d %s",&n,str);
        frnd=0;
        sum=str[0]-'0';
        for(i=1;i<=n;i++)
        {
            if(sum<i)
            {
                frnd+=i-sum;
                sum+=i-sum;
            }
            sum+=str[i]-'0';
            //printf("i:%d sum:%d frnd:%d\n",i,sum,frnd);
        }
        printf("Case #%d: %d\n",x,frnd);
    }
    return 0;
}
