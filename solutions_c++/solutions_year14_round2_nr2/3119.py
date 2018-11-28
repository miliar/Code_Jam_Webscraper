#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("B-small-attempt0.in");
    ofstream out("salida.out");
    int indi,i,j,t,a,b,k,res;
    in>>t;
    for(indi=1;indi<=t;indi++)
    {
     in>>a>>b>>k;
        res=0;
    for(i=0;i<a;i++)
    {
        for(j=0;j<b;j++)
        {
            if((i&j)<k)
            {
                res=res+1;
            }
        }
    }

        out<<"Case #"<<indi<<": "<<res<<endl;
    }

    return 0;
}
