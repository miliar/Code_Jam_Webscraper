#include <cstdio>
#include <algorithm>

using namespace std;

struct tap
{
    double r,tem;
    inline bool operator < (const tap &cpr) const
    {
        return tem<cpr.tem;
    }
};

inline void solvetc(int tcid)
{
    printf("Case #%d: ",tcid);
    int n;
    double v,x;
    scanf("%d%lf%lf",&n,&v,&x);
    tap pos[105];
    for (int i=1; i<=n; i++)
        scanf("%lf%lf",&pos[i].r,&pos[i].tem);
    sort(pos+1,pos+1+n);
    if (pos[1].tem>x || pos[n].tem<x)
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    if (n==1)
    {
        printf("%lf\n",v/pos[1].r);
        return;
    }
    if (n==2)
    {
        if (pos[1].tem==pos[2].tem)
            printf("%lf\n",v/(pos[1].r+pos[2].r));
        else
            if (pos[1].tem==x || pos[2].tem==x)
            {
                if (pos[1].tem==x)
                    printf("%lf\n",v/pos[1].r);
                if (pos[2].tem==x)
                    printf("%lf\n",v/pos[2].r);
            }
            else
                printf("%lf\n",max(v/pos[1].r/(1+(x-pos[1].tem)/(pos[2].tem-x)),v/pos[2].r/(1+(pos[2].tem-x)/(x-pos[1].tem))));
    }
    else
    {
        printf("WAT?\n");
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int it=1; it<=tc; it++)
        solvetc(it);
}
