#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
ifstream f("input.in");
ofstream g("output.txt");

int main()
{
    int t;
    f>>t;
    for(int i=1;i<=t;i++)
    {
        g<<"Case #"<<i<<": ";
        int64_t n;
        f>>n;
        if(!n)
            g<<"INSOMNIA\n";
        else
        {
            vector<int> dig(10);
            bool ok = 1;
            for(int64_t j=1;;j++)
            {
                int64_t m = j*n;
                while(m)
                    dig[m%10]=1,m/=10;
                     if(count(begin(dig),end(dig),0)==0)
                {
                    g<<j*n<<"\n";
                    ok=0;
                    break;
                }
           }
           if(ok)
             g<<"INSOMNIA\n";
        }
    }
}
