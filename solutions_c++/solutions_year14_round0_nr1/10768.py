#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int t,in[5][5],a[20],n;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%d",&n);
        a[0]=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                scanf("%d",&in[i][j]);
                a[i*4+j+1]=0;
            }
        for(int j=0;j<4;j++)
            a[in[n-1][j]]=1;
        scanf("%d",&n);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&in[i][j]);
       int f=0;
       int ans=0;
        for(int j=0;j<4;j++)
        {
            if(a[in[n-1][j]]==1)
            {
                f++;
                ans=in[n-1][j];
            }
        }
        if(f>1)
            printf("Case #%d: Bad magician!\n",k);
        else if(f>0)
            printf("Case #%d: %d\n",k,ans);
        else
            printf("Case #%d: Volunteer cheated!\n",k);
    }
    return 0;
}
