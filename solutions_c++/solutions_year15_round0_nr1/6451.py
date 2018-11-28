#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("Inputlarge1.txt","r",stdin);
    freopen("Outputlarge1.txt","w",stdout);

    int t;
    scanf("%d",&t);
    int smax,i,j,ans,k,s,curr;
    char ch[1005];

    for(i=1;i<=t;i++)
    {
        scanf("%d",&s);
        scanf("%s",ch);

        curr=0;
        curr+=ch[0]-'0';
        ans=0;

        for(j=1;j<=s;j++)
        {
            while(curr<j)
            {
                curr++;
                ans++;
            }
            curr+=ch[j]-'0';
        }
        printf("Case #%d: %d\n",i,ans);
    }

}
