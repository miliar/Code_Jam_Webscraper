#include <cassert>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

#define x first.first
#define y first.second
#define from second
typedef long long ll;
typedef pair< pair<ll, ll> , int > point;
ll ccw(point p0, point p1, point p2)
{
    return p0.x * p1.y + p1.x * p2.y + p2.x * p0.y
        - p0.y * p1.x - p1.y * p2.x - p2.y * p0.x;
}
const int max_n = 1000000;

int n; point p[max_n];
ll calc_area(int *l, int sz)
{
    ll area = 0LL;
    for(int i = 1; i < sz - 1; i++)
        area += ccw(p[l[0]], p[l[i]], p[l[i + 1]]);
    return abs(area);
}

int us; point u[max_n]; int ui[max_n];
int ls; point l[max_n]; int li[max_n];
bool ub[max_n], lb[max_n];
int ua[max_n], la[max_n];

int main()
{
    int T; scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%lld %lld", &p[i].x, &p[i].y);
            p[i].from = i;
        }
        sort(p, p + n);

        us = 0;
        for(int i = 0; i < n; i++)
        {
            while(us >= 2 && ccw(u[us - 2], u[us - 1], p[i]) >= 0)
                us--;
            u[us] = p[i]; ui[us] = i; us++;
        }
        ls = 0;
        for(int i = 0; i < n; i++)
        {
            while(ls >= 2 && ccw(l[ls - 2], l[ls - 1], p[i]) <= 0)
                ls--;
            l[ls] = p[i]; li[ls] = i; ls++;
        }

        for(int i = 0; i < n; i++)
            ub[i] = lb[i] = false;
        int pt;
        assert(us > 1 && ls > 1);
        pt = 1;
        for(int i = 0; i < n; i++)
        {
            while(u[pt].x < p[i].x)
                pt++;
            ub[i] = (ccw(u[pt - 1], u[pt], p[i]) == 0);
        }
        pt = 1;
        for(int i = 0; i < n; i++)
        {
            while(l[pt].x < p[i].x)
                pt++;
            lb[i] = (ccw(l[pt - 1], l[pt], p[i]) == 0);
        }
        int ua_sz = 0;
        for(int i = 0; i < n; i++)
            if(ub[i])
                ua[ua_sz++] = i;
        for(int i = n - 1; i >= 0; i--)
            if(!ub[i])
                ua[ua_sz++] = i;
        int la_sz = 0;
        for(int i = 0; i < n; i++)
            if(lb[i])
                la[la_sz++] = i;
        for(int i = n - 1; i >= 0; i--)
            if(!lb[i])
                la[la_sz++] = i;

        ll tot_area = calc_area(ui, us) + calc_area(li, ls);
        printf("Case #%d:", t);
        if(2 * calc_area(ua, n) > tot_area)
            for(int i = 0; i < n; i++)
                printf(" %d", p[ua[i]].from);
        else if(2 * calc_area(la, n) > tot_area)
            for(int i = 0; i < n; i++)
                printf(" %d", p[la[i]].from);
        else
            assert(false);
        printf("\n");
    }
    return 0;
}
