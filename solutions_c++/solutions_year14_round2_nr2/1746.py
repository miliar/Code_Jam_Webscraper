#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    long long int t, A,B,K,res;
    ifstream in("B.in");
    ofstream out("B.out");
    in>>t;
    for (int Case=1;Case<=t;Case++)
    {
        res=0;
        in>>A>>B>>K;
        for (int i=0;i<A;i++)
            for (int j=0;j<B;j++)
                if ((i&j)<K) res++;
        out<<"Case #"<<Case<<": "<<res<<endl;
    }
}
