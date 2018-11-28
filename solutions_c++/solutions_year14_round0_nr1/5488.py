#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int tt,ii,i,j,k,a[10],b[10],t1,t2;
    scanf("%d",&tt);
    for(ii=1;ii<=tt;ii++)
    {
        scanf("%d",&t1);
        for(i=1;i<=4;i++)
            for(j=0;j<4;j++)
                if(i==t1)
                    scanf("%d",&a[j]);
                else
                    scanf("%d",&k);
        scanf("%d",&t2);
        for(i=1;i<=4;i++)
            for(j=0;j<4;j++)
                if(i==t2)
                    scanf("%d",&b[j]);
                else
                    scanf("%d",&k);
        int cnt=0,ans;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a[i]==b[j])
                {
                    cnt++; ans=a[i];
                    if(cnt>1) break;
                }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",ii);
        else if(cnt==1)
            printf("Case #%d: %d\n",ii,ans);
        else
            printf("Case #%d: Bad magician!\n",ii);
    }
    return 0;
}
