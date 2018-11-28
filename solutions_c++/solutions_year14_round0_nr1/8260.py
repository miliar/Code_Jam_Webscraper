#include <cstdio>
using namespace std;

int a[17];

int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    int t,x,y,i,j,nr;
    scanf("%d",&t);
    for(int k=1;k<=t;++k)
    {
        printf("Case #%d: ",k);
        scanf("%d",&x);
        for(i=1;i<=4;++i)
        {
            if(i!=x) for(j=1;j<=4;++j) scanf("%d",&y);
            else
            {
                for(j=1;j<=4;++j)
                {
                    scanf("%d",&y);
                    ++a[y];
                }
            }
        }
        scanf("%d",&x);
        for(i=1;i<=4;++i)
        {
            if(i!=x) for(j=1;j<=4;++j) scanf("%d",&y);
            else
            {
                nr=0;
                for(j=1;j<=4;++j)
                {
                    scanf("%d",&y);
                    if(a[y])
                    {
                        x=y;
                        ++nr;
                    }
                }
                if(nr==1) printf("%d\n",x);
                if(nr>1) printf("Bad magician!\n");
                if(!nr) printf("Volunteer cheated!\n");
                x=-1;
            }
        }
        for(i=1;i<=16;++i) a[i]=0;
    }
    return 0;
}
