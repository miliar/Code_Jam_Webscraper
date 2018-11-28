#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    in.open("A-small-attempt0 (1).in");
    ofstream out;
    out.open("out.txt");
    int T,t,r;
    int x;
    in>>T;
    for(int n=1; n<=T; n++)
    {
        in>>r>>t;
        int count=0;
        while(t>=0)
        {
            x = (2*r)+1;
            count++;
            t = t-x;
            r = r+2;
        }
        count--;
        out<<"Case #"<<n<<": "<<count<<endl;
    }
    out.close();
}
