#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

int cas=1;
void work()
{
    double farm, pp, tot, p=2.0;
    scanf("%lf%lf%lf", &farm, &pp, &tot);

    double t=0;
    while(pp*tot>(p+pp)*farm)
    {
        t += farm/p;
        p = p+pp;
    }
    t += tot/p;

    printf("Case #%d: %.7lf\n", cas++, t);
}

int main()
{
   // freopen("D:/A-small-attempt0.in", "r", stdin);
   // freopen("D:/out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    while(T--)
        work();
}
