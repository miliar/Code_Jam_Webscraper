#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>

using namespace std;

double calculate(double C, double F, double X)
{
    int i=0;
    double time=0.0,rate=2.0,test1,test2,test3;
    while (i==0)
    {
        test1 = C/rate;
        test2 = X/rate;
        test3 = test1 + (X/(rate+F));
        if (test2<test3)
        {
            time = time + test2;
            i++;
        }
        else
        {
            rate = rate + F;
            time = time + test1;
        }
    }
    return time;
}

int main()
{
    int T,x,i,j;
    double C, F, X,time;
    fstream input;
    fstream output;
    input.open("B-large.txt",ios::in);
    output.open("B-large-out.txt",ios::out);
    output<<setprecision(7)<<fixed;
    input>>T;
    for (x=1;x<=T;x++)
    {
        input>>C>>F>>X;
        time=calculate(C,F,X);
        output<<"Case #"<<x<<": "<<time<<endl;
    }
    input.close();
    output.close();
    return 0;
}
