#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

FILE *in,*out;
int x,y;

#define deb 0

int main() {
    in=fopen("input.in","r");
    ofstream myfile;
    out=fopen("output.out","w");

    int cases;
    fscanf(in,"%d",&cases);

    for(int test=0; test<cases; test++) {
        double c,f,x;
        fscanf(in,"%lf %lf %lf",&c,&f,&x);
        double t1=0;
        double rate = 2.0;
        while(1){
            double time1 = t1 + x/rate;
            double time2 = t1 + c/rate + x/(rate + f);
            if(time1<time2){
                fprintf(out,"Case #%d: %0.7lf\n",test+1,time1);
                break;
            }else{
                t1 += c/rate;
                rate += f;
            }
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}
