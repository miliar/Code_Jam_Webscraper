#include <cstdio>
#include <cstring>

using namespace std;
int i, j, o, t, z, x, y, w, p, a, v[10];
int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);
    scanf("%d", &t);
    memset(v, 0, sizeof(v));
    for(o=1;o<=t;o++)
    {
        scanf("%d", &x);
        w=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                scanf("%d", &z);
                if(i==x)
                {
                    v[j]=z;
                }
            }
        scanf("%d", &y);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                scanf("%d", &z);
                if(i==y)
                {
                    for(p=1;p<=4;p++)
                        if(v[p]==z)
                        {
                            w++;
                            a=z;
                        }
                }
            }
        if(w==1)
            printf("Case #%d: %d\n", o, a);
        else if(w==0)
            printf("Case #%d: Volunteer cheated!\n", o);
        else
            printf("Case #%d: Bad magician!\n", o);
    }
    return 0;
}
