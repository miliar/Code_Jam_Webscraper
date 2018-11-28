#include<stdio.h>
using namespace std;
int  main()
{
FILE* file = fopen ("tp.in", "r");
long long t=0;
fscanf (file, "%lld", &t);
double c,f,x;
for(int a=0;a<t;a++)
    {
        fscanf (file, "%lf", &c);
        fscanf (file, "%lf", &f);
        fscanf (file, "%lf", &x);
        double i,j,k,l;
        i=2;l=0;
        j=x/2;
        while(1)
        {
        k=l+c/i;
        l=l+c/i;
        i=i+f;
        k=k+x/i;
        if(j<k)break;
        else j=k;
        }
        printf("Case #%d: %lf\n",a+1,j);
    }


return 0;
}



