#include <cstdio>
int t, i;
double minim, cp, tant, c, f, x;
void rezolva_problema()
{
    scanf("%d", &t);
    for(i=1;i<=t;++i)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        minim=x/2;
        cp=2;
        tant=0;
        while(tant+(c/cp)+(x/(cp+f))<minim)
        {
            tant+=c/cp;
            cp+=f;
            minim=tant+x/cp;
        }
        printf("Case #%d: %.7lf\n", i, minim);
    }
}
int main()
{
    freopen("cps.in", "r", stdin);
    freopen("cps.out", "w", stdout);
    rezolva_problema();
    return 0;
}
