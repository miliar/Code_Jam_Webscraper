#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main ()
{
    double c,f,x, r=2.0, t1, t2, sum=0;
    int k;
    ifstream fp;
    ofstream op;
    fp.open("test.in");
    op.open("output.in");
    fp.precision(10);
    op.precision(10);
    op<<fixed<<setprecision(7);
    fp>>k;
    for(int i=0; i<k; i++)
    {
    fp>>c>>f>>x;
    while(1)
    {
     t1= x/r;
     t2= (c/r)+(x/(r+f)) ;
     if (t1<t2)
     {
        sum+=t1;
        break;
     }
     sum+=(c/r);
     r+=f;
     }
    op<<"Case #"<<i+1<<": "<<sum<<endl;
    sum=0;
    r=2.0;
    }
    return 0;
}
