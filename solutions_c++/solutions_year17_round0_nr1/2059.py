#include<bits/stdc++.h>

using namespace std;
char a[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas,k;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%s%d",a+1,&k);
        int ans=0,n=strlen(a+1);
        printf("Case #%d: ",tt);
        for (int i=1; i<=n; i++)
            if (a[i]=='-')
            {
                if (i+k-1<=n)
                {
                    ans++;
                    for (int j=i; j<=i+k-1; j++)
                        if (a[j]=='-') a[j]='+'; else a[j]='-';
                }
                else {
                    ans=-1;
                    break;
                }
            }
        if (ans==-1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}




