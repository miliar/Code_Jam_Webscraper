#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

double tot_time(double C, double F, double X, double A, double base, double time )
{
    //double A = X/base;
    double B = C/base;
    double D = X/(base + F);
    if (A < B+D)
        return time + A;
    else
        return tot_time(C, F, X, D, base+F, time + B);
}



int main()
 {
    int i,T;
    double C[100],F[100],X[100], A;
    ifstream File("B-small-attempt2.in");
    File>>T;
    for(i=0;i<T;i++)
        File>>C[i]>>F[i]>>X[i];

    ofstream ofile;
    ofile<<setprecision(7)<<fixed;

    ofile.open("out.txt");

    for(i=0;i<T;i++)
    {
        A = X[i]/2;
        ofile<<"Case #"<<(i+1)<<": "<<tot_time(C[i], F[i], X[i], A, 2.0,0.0)<<endl;
    }
 }


