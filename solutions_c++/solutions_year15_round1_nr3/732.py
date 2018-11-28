#include <bits/stdc++.h>
#define MAXN 10000

using namespace std;

struct point
{
    double x, y;
    int idx;
};

int t, n;
point p[MAXN];
point a[MAXN];
bool is[MAXN];
int N;
point fst;

double turn(point a, point b, point c)
{
    return ((b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x));
}

bool ang_cmp(point a, point b)
{
    return atan2(a.y - fst.y, a.x - fst.x) < atan2(b.y - fst.y, b.x - fst.x);
}

vector<point> hull;
int hullSz;

int mindel[MAXN];

bool GS()
{
    //niz a i veliko n
    N = 0;
    for (int i=1; i<=n; i++)
    {
       if(is[i])
       {
           a[++N] = p[i];
       }
    }
    if(N == 0) return false;

    hull.clear();
    hullSz = 1;

    int f = 1;
    for (int i=2; i<=N; i++)
    {
        if(a[i].y == a[f].y && a[i].x < a[f].x)
            f = i;
        else if(a[i].y < a[f].y)
            f = i;
    }
    fst = a[f];
    swap(a[1], a[f]);
    sort(a+2, a+N+1, ang_cmp);
    a[0] = a[N];

    for(int i=2; i<=N; i++)
    {
        while (turn(a[hullSz-1], a[hullSz], a[i]) < 0)
        {
            if (hullSz >= 2)
            {
                hullSz--;
                continue;
            }
            i++;
            if(i == N+1)
                break;
        }
        hullSz++;
        swap(a[hullSz], a[i]);
    }

    for (int i=0; i<hullSz; i++)
        hull.push_back(a[i]);
}

void Try(int level)
{
    //cout<<level<<endl;
    if(level == n + 1)
    {
        if(!GS()) return;
        for(int i=0; i<hullSz; i++)
        {
           int curr = a[i].idx;
           mindel[curr] = min(mindel[curr], n - N);
        }
        return;
    }
    is[level] = true;
    Try(level + 1);
    is[level] = false;
    Try(level + 1);
    return;
}

int main()
{
    freopen("Cin.txt","r",stdin);
    freopen("Cout.txt", "w", stdout);
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        scanf("%d", &n);
        for(int i=1; i<=n; i++)
        {
            scanf("%lf %lf", &p[i].x, &p[i].y);
            p[i].idx = i;
        }
        for(int i=1; i<=n; i++)
        {
            mindel[i] = n;
        }
        Try(1);
        printf("Case #%d:\n", tt);
        for(int i=1; i<=n; i++)
        {
           printf("%d\n", mindel[i]);
        }
    }
    return 0;
}
