#include<cstdio>
using namespace std;
int a[4][4],n[17];
int main()
{ int t,cnt,i,j,x,X=0,val;
    scanf("%d",&t);
    while(t--)
    { cnt=0;
    X++;
        scanf("%d",&x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(j=0;j<4;j++)
        {
            n[a[x-1][j]]+=1;
        }
        scanf("%d",&x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(j=0;j<4;j++)
        {
             n[a[x-1][j]]+=1;
        }
        for(i=1;i<=16;i++)
        {
            if(n[i]>1)
            {  val=i;
                cnt++;
            }
            n[i]=0;
        }
        if(cnt==1)
        {
            printf("Case #%d: %d\n",X,val);
        }
        if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",X);
        }
        if(cnt>1)
        {
            printf("Case #%d: Bad magician!\n",X);
        }
    }
return 0;
}
