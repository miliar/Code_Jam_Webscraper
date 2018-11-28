#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    //freopen("C:\\Users\\Utkarsh\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\Utkarsh\\Desktop\\output.txt","w",stdout);
    int t,cs;
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++)
    {
        int ar[15][15],r1,r2;
        int mark[20]={0};
        int i,j,k;
        scanf("%d",&r1);
        int cnt=0,temp;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&ar[i][j]);
            }
        }
        for(i=1;i<=4;i++)
            mark[ar[r1][i]]+=1;
        scanf("%d",&r2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&ar[i][j]);
            }
        }
        for(i=1;i<=4;i++)
            mark[ar[r2][i]]+=1;
        for(i=1;i<20;i++)
        {
            if(mark[i]>1)
               {
                   cnt++;
                   temp=i;
               }
        }
        if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",cs);
        }
        else if(cnt==1)
        {
            printf("Case #%d: %d\n",cs,temp);
        }
        else if(cnt>1)
        {
            printf("Case #%d: Bad magician!\n",cs);
        }
    }
    return 0;
}
