#include <bits/stdc++.h>
using namespace std;

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("CJB.txt","w",stdout);
    char a[500],x;
    int t,test,l,i,ans;
    scanf("%d",&test);

    for(t=1;t<=test;t++)
    {
        ans=0;
        scanf(" %s",a);
        l=strlen(a);
        x=a[0];
        for(i=1;i<l;i++)
        {
            if(x!=a[i])
            {
                ans++;
                x=a[i];
            }
        }
        if(x!='+')
            ans++;
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
