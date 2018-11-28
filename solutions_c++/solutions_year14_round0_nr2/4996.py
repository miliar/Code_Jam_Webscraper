#include<iostream>
using namespace std;
#include<iomanip>
#include<stdio.h>
int main()
{
    int t,o;
    double f,c,x;
    cin>>t;
    for(o=1;o<=t;o++)
    {
        cin>>c>>f>>x;
        double init=0.0,inir=2.0,control=0.0,t1temp,t2temp;
        while(control<x)
        {
            t1temp=init+x/inir;
            t2temp=init+c/inir+x/(f+inir);
            if(t1temp>t2temp)
            {
                init=init+c/inir;
                inir=inir+f;
            }
            else
            {
                init=init+x/inir;
                break;
            }

        }
        //cout<<"Case #"<<o<<": "<<setprecision(9)<<init<<"\n";
	printf("Case #%d: %.07f\n",o,init);
    }
    return 0;
}
