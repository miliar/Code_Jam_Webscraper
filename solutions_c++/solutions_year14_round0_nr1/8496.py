#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int k=1;
    while(t--)
    {
        int a,b,p[6][6],q[6][6],pp[20],i,j;
        scanf("%d",&a);
        for(i=1;i<=16;i++)
        {
            pp[i]=0;
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&p[i][j]);
            }
        }
        for(i=1;i<=4;i++)
        {
            pp[p[a][i]]=1;
        }
        scanf("%d",&b);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&q[i][j]);
            }
        }
        for(i=1;i<=4;i++)
        {
            pp[q[b][i]]+=1;
        }
        int cnt=0,ans;
        for(i=1;i<=16;i++)
        {
            if(pp[i]==2) {cnt++;ans=i;}
        }
        if(cnt==1) printf("Case #%d: %d\n",k,ans);
        else if(cnt>1) printf("Case #%d: Bad magician!\n",k);
        else printf("Case #%d: Volunteer cheated!\n",k);
        k++;
    }
    return 0;
}
