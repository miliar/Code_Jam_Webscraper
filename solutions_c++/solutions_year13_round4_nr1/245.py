#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXM (1000+10)
#define mo (1000002013)

struct node
{
    int x, y, p;
};

int n, m, mm;
node a[2*MAXM];
long long tot;
int q[2*MAXM];

bool cmp(node a, node b)
{
    if (a.x < b.x) return true;
    if (a.x > b.x) return false;
    if (a.y < b.y) return true;
    return false;
}

int get(int x, int y)
{
    long long xx, yy, tmp;

    xx = x;
    yy = y;
    tmp = (2*n-xx+1)*xx/2;
    tmp = tmp % mo;
    tmp = (tmp*y) % mo;
    return tmp;
}

void doit()
{
    int r, k,o,e,p;

    tot = 0;
    scanf("%d%d",&n, &m);
    for (int i = 1;i <= m;++i)
    {
        scanf("%d%d%d",&o,&e,&p);
        a[i*2-1].x = o; a[i*2-1].y = 0; a[i*2-1].p = p;
        a[i*2].x = e; a[i*2].y = 1; a[i*2].p = p;
        tot = (tot+get(e-o,p)) % mo;
    }
    sort(a+1, a+m+m+1, cmp);
    r = 0;
    for (int i = 1;i <= 2*m;++i)
    {
        if (a[i].y == 0)
        {
            ++r;
            q[r] = i;
        }
        else {
                while (a[i].p > 0)
                {
                    k = min(a[q[r]].p, a[i].p);
                    tot = (tot-get(a[i].x-a[q[r]].x, k)+mo) % mo;
                    a[i].p -= k;
                    a[q[r]].p -= k;
                    if (a[q[r]].p == 0) --r;
                }
             }
    }

    printf("%d\n",tot);

}

int main()
{
    int t, o, e, p;

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);

    for (int w = 1;w <= t;++w)
    {
        printf("Case #%d: ",w);
        doit();


    }

    return 0;
}
