#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <limits>

using namespace std;

int main(void){
    int t;
    double epsilon = numeric_limits<double>::epsilon();
    double C, F, X;
    double v,ut,lt,tb;    
    FILE *in,*out;
//    in=fopen("in.txt","r");
//    in=fopen("B-small-attempt0.in","r");
    in=fopen("B-large.in","r");
    out=fopen("out.txt","w");
    fscanf(in,"%d",&t);
    for (int i=1;i<=t;i++){
        fscanf(in,"%lf %lf %lf",&C, &F, &X);   
        tb=0;
        lt=-1;
        ut=-1;
        v=2;
        do{
           lt=ut;
           ut=tb+(X/v);
           tb+=C/v;
           v+=F;
           }while (lt==-1||ut<lt);
        fprintf(out,"Case #%d: %.7lf\n",i,lt);
        }
    fclose (in);
    fclose (out);
    return 0;
    }
