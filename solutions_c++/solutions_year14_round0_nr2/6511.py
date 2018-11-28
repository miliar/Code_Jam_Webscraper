#include <iostream>
#include <fstream>
using namespace std;

double fun(long double x, long double f, long double c,long double inc,long double t)
{
    while(!(x/inc < ((x/(inc+f))+(c/inc))))
    {
        t = t+ c/inc;
        inc = inc+f;
    }

    t = t + x/inc;
    return t;
}

int main()
{
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("out.txt");
    long double T,x,f,c,inc,time;
    in>>T;
    for(int t=1; t<=T; t++)
    {
        in>>c>>f>>x;
        inc = 2;
        time = 0;
        out.precision(10);
        out<<"Case #"<<t<<": "<<fun(x,f,c,inc,time)<<endl;
    }
    in.close();
    out.close();
    return 0;
}
