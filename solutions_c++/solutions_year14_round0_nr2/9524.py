#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

double c, f, x;

double compute(double rate)
{
    if ( (x/rate) > ( (c/rate) + ( x/ (rate+f) ) ) )
    {
        return ((c/rate) + compute(rate+f));
    }
    else
    {
        return (x/rate);
    }
}

int main()
{
    fstream f1, f2;
    f1.open("B-small.in", ios::in);
    f2.open("output.txt", ios::out | ios::binary);
    int num;
    f1>>num;
    for (int i=0; i<num; i++)
    {
        f1>>c;
        f1>>f;
        f1>>x;
        f2<<"Case #"<<(i+1)<<": "<<fixed<<setprecision(7)<<compute(2.00)<<endl;
    }
    f1.close();
    f2.close();
    return 0;
}
