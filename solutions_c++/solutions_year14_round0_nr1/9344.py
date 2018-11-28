#include <bits/stdc++.h>
using namespace std;


int main()
{
    int a[4][4],b[4][4];
    int n,m,d,j,i,k,tt,t;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        scanf("%d",&n);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        d=-1;k=-1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[n-1][i]==b[m-1][j] && d == -1)
                    d = a[n-1][i];
                else if(a[n-1][i]==b[m-1][j] && d != -1)
                    k = a[n-1][i];
            }
        }
        if(d==-1)
            printf("Case #%d: Volunteer cheated!\n",tt);
        else if(d!=-1 && k==-1)
            printf("Case #%d: %d\n",tt,d);
        else 
            printf("Case #%d: Bad magician!\n",tt);

    }
    return 0;
}
