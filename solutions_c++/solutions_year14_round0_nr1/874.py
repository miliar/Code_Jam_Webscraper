#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,tc;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        int i,j,a,arr[5][5];
        int hasharr[20];
        for(i=1;i<=16;i++)
            hasharr[i]=0;
        scanf("%d",&a);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&arr[i][j]);
        for(i=1;i<=4;i++)
            hasharr[arr[a][i]]++;
        scanf("%d",&a);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&arr[i][j]);
        for(i=1;i<=4;i++)
            hasharr[arr[a][i]]++;
        int cnt=0,ans;
        for(i=1;i<=16;i++)
            if(hasharr[i]==2)
            {
                cnt++;
                ans=i;
            }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",tc);
        else if(cnt==1)
            printf("Case #%d: %d\n",tc,ans);
        else
            printf("Case #%d: Bad magician!\n",tc);
    }
    return 0;
}
