#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    int ln_t;
    double ld_c, ld_f, ld_x, ld_g;
    double ld_ans;
    scanf("%d",&ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        ld_g = 2;
        scanf("%lf%lf%lf", &ld_c, &ld_f, &ld_x);
        double td_g_up = ld_f*(ld_x-ld_c)/ld_c;
        ld_ans = 0;
        for (;ld_g<td_g_up;ld_g+=ld_f)
        {
            ld_ans += ld_c/ld_g;
//            printf("~~ %.7f\n", ld_ans);
        }
        ld_ans += ld_x/ld_g;
        printf("Case #%d: %.7f\n", ln_cas, ld_ans);
    }
    return 0;
}
