#include <iostream>
#include <cstdio>
#include <iomanip>
#include <fstream>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("PB.out");
int T;
double C,F,X;
double calculate(int t){
    double rtn=0;
    for(int o=0;o<t;o++){
        rtn+=C/(2+o*F);
    }
    rtn+=X/(2+t*F);
    return rtn;
}
int main()
{
    fin>>T;
    for(int t=1;t<=T;t++){

        fin>>C>>F>>X;

        int lmt=200000;

        int a=0,b=lmt/3,c=lmt*2/3,d=lmt;

        double fa,fb,fc,fd;

        while(d-a>2)
        {

            b=(d*1+a*2)/3,c=(d*2+a*1)/3;

            fa=calculate(a);
            fb=calculate(b);
            fc=calculate(c);
            fd=calculate(d);

            if(fa>=fb&&fb>=fc&&fc>=fd){
                a=b;
            }
            if(fa>=fb&&fb>=fc&&fc<=fd){
                a=b;
            }

            if(fa>=fb&&fb<=fc&&fc<=fd){
                d=c;
            }
            if(fa<=fb&&fb<=fc&&fc<=fd){
                d=c;
            }

        }
        fout<<"Case #"<<t<<": ";
        double ans=min(fa,min(fb,min(fc,fd)));


        fout<<fixed<<setprecision(7)<<ans<<endl;
    }
}
