#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

FILE *in = fopen("B.in","r");
FILE *out = fopen("B.out","w");

int main () {
    int t,k=1;
    fscanf (in,"%d",&t);
    while (t --) {
        double C,F,X;
        fprintf (out,"Case #%d: ",k++);
        fscanf (in,"%lf",&C);
        fscanf (in,"%lf",&F);
        fscanf (in,"%lf",&X);
        double ret = 50005.0;
        double farms = 0.0;
        double r = 2.0;
        while (1) {
            double direct = X / r;
            double comp = farms + direct;
            if (ret <= comp) break;
            ret = comp;
            farms += C / r;
            r += F;
        }
        fprintf (out,"%.7lf\n",ret);
    }
}
