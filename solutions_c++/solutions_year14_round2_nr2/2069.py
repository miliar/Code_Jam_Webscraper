#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

typedef int64_t lint;
int main()
{
    fstream in("B-small-attempt0.in");
    fstream out("out.txt");
    int t;
    in>>t;
    for(int z=1;z<=t;z++)
    {
        lint A,B,K;
        in>>A>>B>>K;

        lint ans=0;
        for(lint i=0;i<A;i++)
        {
            for(lint j=0;j<B;j++)
            {
                if((i&j)<K){ans++;}
            }
        }
        out<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;

}
