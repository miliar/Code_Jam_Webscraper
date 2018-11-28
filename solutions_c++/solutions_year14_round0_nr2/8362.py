#include<iostream>
#include<fstream>
#include <iomanip>
#include <limits>
#include <math.h>

using namespace std;

int main()
{
    long double c[100],f[100],x[100];

    int n,e=0;

    long double a,b,d;
    long double sum=0;



    ifstream infile;
    infile.open("sub-3.in");
    infile>>n;

    ofstream out;
    out.open("cook.txt");






for(int j=0;j<n;j++)
{
    infile>>c[j]>>f[j]>>x[j];
}


        for(int j=0;j<n;j++)
        {

            sum=0;


            for(double i=2; ;i=i+f[j])
            {
                    a=c[j]/i;
                    b=x[j]/i;
                    d=x[j]/(i+f[j]);

                if(a+d<b)
                {
                    sum=sum+a;
                    //cout<<a<<"\n"<<d<<"\n"<<sum<<"\n";

                }

                else
                    break;


                //cout<<a<<"\n"<<d<<"\n";
            }

            //out<<setprecision(10);






            out<<"Case #"<<e+1
                <<":"<<" "<< setprecision (7)<<fixed<<sum+b<<"\n";
            e++;


        }















    return 0;
}
