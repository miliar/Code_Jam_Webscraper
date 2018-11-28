#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,ans,sum,flag;
    flag=0;
    char S[1001];
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        sum=0;
        ans=0;
        scanf("%d %s",&n,S);
        printf("Case #%d: ",c);
        sum=S[0]-'0';
        for(int i=1;i<=n;i++)
        {
            flag=0;
            //printf("before %d %d %d %d        ",i,sum,ans,flag);
            if(i>sum && S[i]-'0'>0)
            {
                ans=ans+(i-sum);
                sum=i+S[i]-'0';
                flag=1;
            }
            if(flag==0)
            {
                sum=sum+S[i]-'0';
            }
            //printf("after %d %d %d %d\n",i,sum,ans,flag);
        }
        printf("%d\n",ans);
    }
    return 0;
}
