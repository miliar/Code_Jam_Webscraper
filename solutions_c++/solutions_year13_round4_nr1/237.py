#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
using namespace std;

struct cos
{
    long long ilu, kie;

    friend bool operator < (cos a, cos b)
    {
        return a.kie<b.kie;
    }
};

priority_queue<cos> mam;
cos wys[1005], wsi[1005];

int main ()
{
    long long w, w2, mod=1000002013, a, b, c, z, n, m, d, e, f;
    cos kaka;

    scanf ("%lld", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%lld %lld", &n, &m);
        e=w=w2=0;

        for (b=0; b<m; b++)
        {
            scanf ("%lld %lld %lld", &wsi[b].kie, &wys[b].kie, &d);
            wys[b].ilu=wsi[b].ilu=d;
            c=wys[b].kie-wsi[b].kie;
            c*=(long long)2*n+(long long)1-c;
            c/=(long long)2;
            c%=mod;
            c*=d;
            c%=mod;
            w+=c;
            w%=mod;
        }

        sort(wys,wys+m);
        sort(wsi,wsi+m);
        b=0;
        c=0;

        while (b<m || c<m)
        {
            if (b<m && wsi[b].kie<=wys[c].kie)
            {
                mam.push(wsi[b]);
                b++;
            }
            else
            {
                d=wys[c].ilu;

                while (d)
                {
                    kaka=mam.top();
                    mam.pop();
                    e=wys[c].kie-kaka.kie;

                    if (kaka.ilu>=d)
                    {
                        e*=(long long)2*n+(long long)1-e;
                        e/=(long long)2;
                        e%=mod;
                        e*=d;
                        e%=mod;
                        w2+=e;

                        if (w<0)
                            w2+=mod;

                        w2%=mod;
                        kaka.ilu-=d;

                        if (kaka.ilu)
                            mam.push(kaka);

                        d=0;
                    }
                    else
                    {
                        e*=(long long)2*n+(long long)1-e;
                        e/=(long long)2;
                        e%=mod;
                        e*=kaka.ilu;
                        e%=mod;
                        w2+=e;

                        if (w2<0)
                            w2+=mod;

                        w2%=mod;
                        d-=kaka.ilu;
                    }
                }

                c++;
            }
        }

        w-=w2;

        if (w<0)
            w+=mod;

        printf ("Case #%lld: %lld\n", a, w);
    }

    getchar();
    getchar();
    return 0;
}
