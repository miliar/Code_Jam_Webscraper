#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
using namespace std;
int t,n,x,ar[10005];
bool temp[10005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for (int ll=1;ll<=t;ll++){
        scanf("%d %d",&n,&x);

        for (int i=1;i<=n;i++)
            scanf("%d",&ar[i]);

        sort(ar+1,ar+n+1);
        int ans=0;
        memset(temp,0,sizeof(temp));
        for (int i=n;i>=1;i--)
            if (temp[i]==0){
                ans++;
                temp[i]=1;
                for (int j=i-1;j>=1;j--)
                    if (ar[i]+ar[j]<=x && temp[j]==0)
                    {
                        temp[j]=1;
                        break;
                    }
            }

        printf("Case #%d: %d\n",ll,ans);
    }

    return 0;
}
