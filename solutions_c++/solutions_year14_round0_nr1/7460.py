#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int t,i,a,b,j,k,a1[4][4],a2[4][4],cnt,ans;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        scanf("%d",&a);
        a--;
        for(j=0;j<4;++j)
        {
            for(k=0;k<4;++k)
            {
                scanf("%d",&a1[j][k]);
            }
        }
        scanf("%d",&b);
        b--;
        for(j=0;j<4;++j)
        {
            for(k=0;k<4;++k)
            {
                scanf("%d",&a2[j][k]);
            }
        }
        cnt=0;
        for(j=0;j<4;++j)
        {
            for(k=0;k<4;++k)
            {
                if(a1[a][j]==a2[b][k])
                {
                    cnt++;
                    ans=a1[a][j];
                }
            }
        }
        if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",i);
        }
        else if(cnt==1)
        {
            printf("Case #%d: %d\n",i,ans);
        }
        else if(cnt>1)
        {
            printf("Case #%d: Bad magician!\n",i);
        }
    }
    return 0;
}
