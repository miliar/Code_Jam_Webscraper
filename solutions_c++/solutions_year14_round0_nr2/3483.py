#include<iostream>
#include<cstdlib>
#include<fstream>
#include <iomanip>
using namespace std;
double compute(double c,double f,double x)
{
    double r=2,t1,t2,tim=0;
    while(1)
    {
        t1=x/r;
        t2=((c/r) + (x/(r+f)));
        if(t1<t2)
        {
            tim+=t1;
            return tim;
        }
        else
        {
            tim+=(c/r);
            r+=f;
        }
    }

}
int main()
{
    fstream f1,f2;
    int i,j,k,n1;
    double c,f,k1;
    f1.open("B-large.in",ios::in);
    f2.open("op4.txt",ios::out);
    f1>>n1;
    for(k=0;k<n1;k++)
    {
        f1>>c;
        f1>>f;
        f1>>k1;
        double tim=compute(c,f,k1);
        f2<<"Case #"<<k+1<<": ";
        f2<< fixed << setprecision(7)<<tim<<"\n";
        // cout<<c<<"  "<<f<<"  "<<k1<<"\n";
    }
    f1.close();
    f2.close();
    return 0;
}
