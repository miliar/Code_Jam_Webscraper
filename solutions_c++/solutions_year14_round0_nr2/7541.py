#include<iostream>
#include<fstream>
#include<cstdlib>
#include<stdio.h>
#include<iomanip>
using namespace std;
ifstream in("in.in");
ofstream out("output.txt");
int T;
double c, f, x;

double div(double a, double b)
{
    return a/b;
}

int main()
{
    in>>T;
    for(int i=0;i<T;i++)
    {
        in>>c>>f>>x;
        long double cps=2;
        long double sProssimaF, sVittoria;
        long double somma=0;
        long double sommaP=0;
        long double lsommaP=99999999;
        do
        {
            sProssimaF=div(c,cps);
            sVittoria=div(x,cps);
            sommaP=somma+sVittoria;
            if(sommaP>=lsommaP)
            {
                break;
            }
            cps+=f;
            somma+=sProssimaF;
            cout<<sProssimaF<<":"<<sVittoria<<endl;
            cout<<somma<<endl;
            lsommaP=sommaP;
            //system("pause");
        }while(true);
        out<<"Case #"<<i+1<<": "<< std::fixed << std::setprecision(7) <<lsommaP <<endl;
    }
    in.close();
    out.close();
}
