#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
ifstream fin ("input");
ofstream fout ("output");

int main()

{

    long T,t,i,j;
    double C,F,X,sec,secmin,f;
    fin>>T;
    t=T;
    while(T>0)
    {
        sec=0;secmin=-1;
        fin>>C>>F>>X;
        fout<<"Case #"<<t-T+1<<": ";
        for(i=0;i<=floor(X/C);i++)
        {
            sec=0;f=2;
            for(j=0;j<i;j++)
                {sec+=C/f;f+=F;}
            sec+=X/f;

            if(secmin>sec||secmin==-1)secmin=sec;
        }

        fout.setf(ios::fixed,ios::floatfield);
        fout.precision(7);
        fout<<secmin;
        fout<<endl;
        T--;
    }
    return 0;
}

