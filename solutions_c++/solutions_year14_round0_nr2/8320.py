#include <stdio.h>
#include <algorithm>
using namespace std;
main()
{
    int i,j,k;

    int t;
    FILE *in = fopen("B.in","r");
    FILE *out = fopen("B.out","w");
    fscanf(in,"%d",&t);

    for (i=1;i<=t;i++) {


    double X,C,F;

    fscanf(in,"%lf%lf%lf",&C,&F,&X);


    double tot=0;
    double low = X/2;
    int n;
    for (n=1;n<=100000;n++) {
        tot+=C/(2+(n-1)*F);
        low=min(low,tot+X/(2+n*F));
    }

    fprintf(out,"Case #%d: %.7lf\n",i,low);
    }

}
