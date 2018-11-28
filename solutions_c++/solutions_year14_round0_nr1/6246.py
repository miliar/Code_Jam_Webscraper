#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int a[6][6],b[6][6];

int main()
{
    int T,t,i,j,ans1,ans2;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output-A.out","w",stdout);
    while(~scanf("%d",&T))
    {
        for(t=1;t<=T;t++)
        {
            scanf("%d",&ans1);
            for(i=1;i<=4;i++)
                for(j=1;j<=4;j++)
                    scanf("%d",&a[i][j]);
            scanf("%d",&ans2);
            for(i=1;i<=4;i++)
                for(j=1;j<=4;j++)
                    scanf("%d",&b[i][j]);
            int cnt=0,out=-1;
            for(i=1;i<=4;i++)
            {
                for(j=1;j<=4;j++)
                {
                    if(a[ans1][i]==b[ans2][j]){
                        cnt++;
                        out=a[ans1][i];
                    }
                }
            }
            if(cnt==1)
                printf("Case #%d: %d\n",t,out);
            else if(cnt==0)
                printf("Case #%d: Volunteer cheated!\n",t);
            else if(cnt>1)
                printf("Case #%d: Bad magician!\n",t);
        }
    }
    return 0;
}
