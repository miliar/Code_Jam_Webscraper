#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("outputx.in");
    int T,count=0;
    double C,F,X,cookie=0,x=0,rate=2,j,temp,sol=0;
    fin>>T;
    fin.precision(10);
    for(int i=0;i<T;i++)
    {
            fin>>C;
            fin>>F;
            fin>>X;
            while(1)
            {
                cookie=(C/rate)+(X/(rate+F));
                temp=(X/rate);
                if(temp<cookie)
                {
                    sol+=temp;
                    break;
                }
                sol+=(C/rate);
                rate=rate+F;
            }
            fout<<"\nCase #"<<i+1<<": ";
            fout.precision(10);
            fout<<std::showpoint<<sol;
            sol=0;
            rate=2;
    }
    return 0;
}
