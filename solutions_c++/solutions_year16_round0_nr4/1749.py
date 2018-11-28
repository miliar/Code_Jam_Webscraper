#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("in.in");
    out.open("out.txt");
    int T,S,C,K;
    in>>T;
    int t;
    for(t=1;t<=T;t++)
    {
        in>>K>>C>>S;
        out<<"Case #"<<t<<":";
        for(int i=1;i<=S;i++)
        {
            out<<" "<<i;
        }
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
