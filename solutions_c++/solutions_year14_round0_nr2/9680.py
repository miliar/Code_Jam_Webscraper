#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("cookieclickeralpha.in","r",stdin);
    freopen("cookieclickeralpha1.out","w",stdout);
    int t, t1=0;
    scanf("%d",&t);
    while (t--) {
    t1++;
    double c,f,x;
    scanf("%lf%lf%lf",&c,&f,&x);
    int i,j;
    double min1=10000000000.0;
    // kolku farmi
    for (i=0;i<=5000;i++) {
        double br=0.0;

        double kolaci=2;
        for (j=0;j<i;j++) {
            br+= (double)c / (double)kolaci;
            kolaci += f;
        }
        br+= (double)x / kolaci;

        if (br<min1) min1=br;
    }
    printf("Case #%d: %.7lf\n", t1, min1);
    }
    return 0;
}
