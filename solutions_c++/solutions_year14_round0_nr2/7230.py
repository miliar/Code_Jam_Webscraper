#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    double c=0,f=0,x=0,CpS=2.0,elapsed=0.0;
    int farms=0,t;
    ifstream ifile ("input.in");
    ifile >> t;
    double minresult[t];
    for(int i=0;i<t;i++)
    {
        ifile >> c >> f >> x;
        minresult[i] = x/CpS;
        bool ready=true;
        do
        {
            double result=0;
            elapsed+=c/CpS;
            CpS += f;
            result = (x/CpS)+elapsed;
            if(result<minresult[i])
            {
                ready = false;
                minresult[i]=result;
            }
            else
            {
                ready = true;
            }
        }
        while(ready==false);
        elapsed=0.0;
        CpS=2.0;
    }
    ofstream ofile ("output.out");
    for(int i=0;i<t;i++)
    {
        ofile << "Case #"<<i+1<<": ";
        ofile <<fixed<<setprecision(7)<<minresult[i]<< endl;
    }
}
