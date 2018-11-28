#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

FILE *src = fopen("data.txt","r");
FILE *dest = fopen("data.out","w");

void cal(double C,double F,double X)
{
    double current_p = 2.0000000;
    double totaltime = 0.0000000;
    while ((X-C)/current_p > X/(current_p+F))
    {
        totaltime += C/current_p;
        current_p += F;
    }
    totaltime += X/current_p;
    fprintf(dest,"%.7lf\n",totaltime);

}

int main()
{
    int T,i;
    double C,F,X;
    fscanf(src,"%d",&T);
    for (i = 1; i <= T; ++i)
    {
        fscanf(src,"%lf",&C);
        fscanf(src,"%lf",&F);
        fscanf(src,"%lf",&X);
        fprintf(dest,"Case #");
        fprintf(dest,"%d",i);
        fprintf(dest,": ");
        cal(C,F,X);
    }
    return 0;
}
