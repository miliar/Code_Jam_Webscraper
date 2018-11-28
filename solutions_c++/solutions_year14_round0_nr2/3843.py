#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    int t,i,j,k;
    double c,f,x,ti=0.0,ti1=0.0,ti2;
    input>>t;
    for(i=0;i<t;i++)
    {
        input>>c>>f>>x;
        ti=x/2.0;
        ti1=0.0;
        for(j=1;;j++)
        {
            ti1+=c/((j-1)*f+2.0);
            ti2=ti1+(x/(j*f+2.0));
            if(ti2>=ti)
            break;
            ti=ti2;
        }
        output.precision(7);
        output.setf(ios::fixed);
        output.setf(ios::showpoint);
        output<<"Case #"<<i+1<<": "<<ti<<endl;
    }
    return 0;
}
