#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    ifstream Cin("inn.in");
    ofstream Cout("out.txt");

    unsigned long long int tc,i,res,q,r,l;Cin>>tc;

    for(i=0;i<tc;i++)
    {
        Cin>>r>>l;
        q=0;res=0;
        for(unsigned long long int j=r;q<l;j=j+2)
        {
            q= 1+(2*j) + q;
            if(q<=l)
            res++;
        }
        Cout<<"Case #"<<i<<": "<<res<<"\n";


    }

}
