#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
//#define fin cin
//#define fout cout
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");
    int r;
    fin>>r;
    for(int k=1;k<=r;++k)
    {
        double C, F, X, time, mn=2e9;
        fin>>C>>F>>X;
        for(int t=0;;++t)
        {
            time=0.0;
            for(int i=1;i<=t;++i)
            {
                time+=(C/(2+F*(i-1)));
            }
            time+=X/(2+F*t);
            if(time<mn)mn=time;
            else if(time>mn)break;
        }
        fout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<mn<<endl;
    }
    return 0;
}
