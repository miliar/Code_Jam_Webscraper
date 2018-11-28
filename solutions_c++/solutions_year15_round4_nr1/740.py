#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

char t[100][100];
int ile[100],ilek[100];
int piew[100],piek[100],ostw[100],ostk[100];

int main ()
{
    int a,b,c,d,e,f,g,n,z,w;
    char x;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        for (b=0; b<100; b++)
        {
            ile[b]=ilek[b]=0;
            piew[b]=piek[b]=101;
            ostw[b]=ostk[b]=-1;
        }

        scanf ("%d%d", &b, &c);
        w=0;

        for (d=0; d<b; d++)
        {
            getchar();

            for (e=0; e<c; e++)
            {
                t[d][e]=getchar();

                if (t[d][e]!='.')
                {
                    ile[d]++;
                    ilek[e]++;
                    piew[d]=min(piew[d],e);
                    piek[e]=min(piek[e],d);
                    ostw[d]=max(ostw[d],e);
                    ostk[e]=max(ostk[e],d);
                }
            }
        }

        for (d=0; d<b; d++)
        {
            for (e=0; e<c; e++)
                if (t[d][e]!='.')
                {
                    if (ile[d]==1 && ilek[e]==1)
                        break;

                    if (piew[d]==e && t[d][e]=='<')
                    {
                        w++;
                        continue;
                    }

                    if (piek[e]==d && t[d][e]=='^')
                    {
                        w++;
                        continue;
                    }

                    if (ostw[d]==e && t[d][e]=='>')
                    {
                        w++;
                        continue;
                    }

                    if (ostk[e]==d && t[d][e]=='v')
                    {
                        w++;
                        continue;
                    }
                }

            if (e<c)
                break;
        }

        if (d<b)
        {
            printf ("Case #%d: IMPOSSIBLE\n", a);
            continue;
        }

        printf ("Case #%d: %d\n", a, w);
    }

    return 0;
}
