#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    ifstream fin;
    fstream fout;
    fin.open("input.txt",ios::in);
    fout.open("output.out",ios::out);
    long double C =0.0, F=0.0, X=0.0,time=0,time2=0,time3=0,r=2.0, r2=0.0,T=0.0;
    fin>>T;
    for(unsigned long long int n=0;n<T;n++)
    {
        time=0;
        r=2.0;
        fin>>C>>F>>X;
         while(1)
        {
            time2=X/r;

            time3=C/r;
            r2=r+F;
            time3+=X/r2;

            if(time2<=time3)
            {
                time+=time2;
                break;
            }
            else
            {
                time+=C/r;
                r=r2;
            }
        }
        cout.setf(ios::fixed);
        cout.setf(ios::showpoint);
        fout.setf(ios::fixed);
        fout.setf(ios::showpoint);
        cout<<"Case #"<<n+1<<": "<<setprecision(7)<<time<<endl;
        fout<<"Case #"<<n+1<<": "<<setprecision(7)<<time<<endl;

    }
    return 0;
}
