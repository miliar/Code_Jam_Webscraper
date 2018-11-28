#include<cstdio>
#include<cstring>
using namespace std;
int t,o,i,j,x,x1,p,z,v[17];
int main()
{
    //freopen("MT.in","r",stdin);
    //freopen("MT.out","w",stdout);
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        scanf("%d",&x);
        memset(v,0,sizeof(v));
        z=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&x1);
                if(i==x)v[x1]++;
            }
        }
        scanf("%d",&x);
        p=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&x1);
                if(i==x&&v[x1]==1){z++;p=x1;}
            }
        }
        if(z==1)printf("Case #%d: %d\n",o,p);
        else if(z>1)printf("Case #%d: Bad magician!\n",o);
        else if(z==0)printf("Case #%d: Volunteer cheated!\n",o);
    }
    return 0;
}

