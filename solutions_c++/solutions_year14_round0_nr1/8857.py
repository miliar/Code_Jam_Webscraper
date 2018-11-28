#include <cstdio>

using namespace std;

int T,t,i,j,k,x,y,sol,nr,a[100];
int main()
{
    scanf("%d", &T);
    for(t=1;t<=T;++t)
    {
        sol=0;nr=0;
        scanf("%d", &x);
        for(i=1;i<=4;++i)
            for(j=1;j<=4;++j)
            {
                scanf("%d", &y);
                if(i==x)
                    a[j]=y;
            }
        scanf("%d", &x);
        for(i=1;i<=4;++i)
            for(j=1;j<=4;++j)
            {
                scanf("%d", &y);
                if(i==x)
                {
                    for(k=1;k<=4;++k)
                        if(y==a[k])
                        {
                            sol=y;
                            nr++;
                        }
                }
            }
        if(nr==0)printf("Case #%d: Volunteer cheated!\n", t);
        if(nr==1)printf("Case #%d: %d\n", t, sol);
        if(nr>=2)printf("Case #%d: Bad magician!\n", t);


    }
    return 0;
}
