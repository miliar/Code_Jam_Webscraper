#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,x,y,ii;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%d",&x);

        int ma[17],a[4][4],b[4][4],i,j,count=0,val;
        for(i=0;i<17;i++)
            ma[i]=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        for(i=0;i<4;i++)
            ma[a[x-1][i]]++;
        for(i=0;i<4;i++)
        {
            if(ma[b[y-1][i]]>0)
            {
                count++;
                val=b[y-1][i];
            }
        }
        if(count==1)
            printf("Case #%d: %d\n",ii,val);
        else if(count>1)
            printf("Case #%d: Bad magician!\n",ii);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",ii);
    }
    return 0;
}
