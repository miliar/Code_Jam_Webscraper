#include<iostream>
#include<iomanip>
#include<cstdio>
#include<fstream>
using namespace std;
double C,F,X;
int T;
double EPS= 1e-12;
int main()
{
    fstream fin("B-large.in");
    fstream fout("B-large.out");
    fin>>T;
    int Ct=1;
    while(T--)
    {
        fin>>C>>F>>X;
        double Counter=2.0;
        double ans=0;
        while(1)
        {
            double temp=C/Counter;
            double pemp=X/Counter;
            if((pemp-(temp+(X/(Counter+F))))>=EPS)
            {
                ans+=temp;
                Counter+=F;
            }
            else
            {
                ans+=pemp;
                break;
            }
          }
        fout<<"Case #"<<Ct++<<": ";
        fout <<std::setprecision(7)<<ans<<endl;
    }
    return 0;
}
