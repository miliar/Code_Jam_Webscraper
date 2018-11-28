#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    long double C,F,X,S,T;
    ifstream in("B.in");
    ofstream out("B.out");
    in>>t;
    for (int i=0;i<t;i++)
    {
        S=2;
        T=0;
        in>>C>>F>>X;
        while(C/S+X/(S+F)<X/S)
        {
            T+=C/S;
            S+=F;
        }
        T+=X/S;
        out<<"Case #"<<i+1<<": "<<fixed<<setprecision(8)<<T<<endl;
    }


    return 0;
}
