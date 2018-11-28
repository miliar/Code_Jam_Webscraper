#include<bits/stdc++.h>
using namespace std;
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("BL1.txt","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        char s[105];
        scanf("%s",s);
        int l=strlen(s),ct=0,j;
        for( j=l-1;j>=0;j--)
        {
            if(s[j]=='-')
                break;
        }
        if(j>=0)
        {
            int d=0;
            for(int k=1;k<=j;k++)
            {
                if(s[k-1]!=s[k])
                    d++;
            }
            printf("Case #%d: %d\n",i,d+1);
            continue;
        }
        printf("Case #%d: 0\n",i);
    }

    return 0;
}
