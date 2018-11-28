#include <stdio.h>
#include <cstdlib>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *o = fopen("output.txt","w");
    int t;
    fscanf(in,"%d",&t);
    for(int i=0; i<t; i++)
    {
            double time = 0.0000000;
            double v = 2.0000000;
            double c,f,x;
            fscanf(in,"%lf%lf%lf",&c,&f,&x);
            while((x / v) > ((c / v) + (x / (v + f))))
            {
                     time += c / v;
                     v += f;
            }
            time += x / v;
            fprintf(o,"Case #%d: %.7lf\n",i+1,time);
    }
}
