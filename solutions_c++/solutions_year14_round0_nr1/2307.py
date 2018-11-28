#include <iostream>
#include<cstdio>
using namespace std;

int b[20];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,x,i,y,c,ans,tt,j;
    scanf("%d",&test);
    for(tt=1;tt<=test;tt++)
    {
        for(i=0;i<=17;i++)
        b[i]=0;
        c=0;
        scanf("%d",&x);
        x--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&y);
                if(i==x)
                b[y]++;
            }
        }
        scanf("%d",&x);
        x--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&y);
                if(i==x)
                b[y]++;
            }
        }
        for(i=1;i<=16;i++)
        {
            if(b[i]==2)
            {
                c++;
                ans=i;
            }
        }
        printf("Case #%d: ",tt);
        if(c==1)
        printf("%d\n",ans);
        else if(c>1)
        printf("Bad magician!\n");
        else if(c==0)
        printf("Volunteer cheated!\n");
    }
    return 0;
}
