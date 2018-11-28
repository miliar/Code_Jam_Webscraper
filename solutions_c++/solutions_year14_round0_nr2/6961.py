#include <iostream>
#include<iomanip>
#include<fstream>
using namespace std;

int main()
{

int test,i=0;double cookie=2;
double C,F,X,sec=0;
ifstream in;
ofstream out;
in.open("input.txt");
out.open("output.txt");
while(in.good())
{

in>>test;
while(i<test)
{
    in>>C>>F>>X;
    while(1)
    {
        if((X/cookie)<((C/cookie)+(X/(cookie+F))))
        {
            sec=sec+(X/cookie);
            break;

        }
        else
        {
            sec=sec+(C/cookie);
           //out<<"time after divide "<<sec<<"\n";
            cookie=cookie+F;
            //out<<"cookies after divide "<<cookie<<"\n";

        }
    }

    out<<"Case #"<<i+1<<": ";
    out.precision(7);
    out.setf(ios::fixed);
    out.setf(ios::showpoint);
    out<<sec<<"\n";
    sec=0;
    cookie=2;
    i++;
}
in.close();
out.close();
}
    return 0;
}
