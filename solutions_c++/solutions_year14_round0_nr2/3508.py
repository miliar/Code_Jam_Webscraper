#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t, cas=1;
double c, f, x, cs, ans;

int main(void)
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf %lf %lf", &c, &f, &x);

        cs=2;
        ans=0;
        while(x/cs>c/cs+x/(cs+f))
        {
            ans+=c/cs;
            cs+=f;
        }
        ans+=x/cs;

        printf("Case #%d: %.7lf\n", cas++, ans);

    }

    return 0;
}
