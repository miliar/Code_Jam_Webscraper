#include <iostream>
#include <fstream>
#include <cmath>
typedef unsigned long long int ull;

using namespace std;
ull isqrt32 (ull n)
{
    ull root, remainder, place;
    root = 0;
    remainder = n;
    place = 0x40000000;
    while (place > remainder)
            place = place >> 2;
    while (place)
    {
            if (remainder >= root + place)
            {
                    remainder = remainder - root - place;
                    root = root + (place << 1);
            }
            root = root >> 1;
            place = place >> 2;
    }
    return root;
}
int main()
{
    ull T,r,t,c;
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin>>T;
    for(ull x=0;x<T;x++)
    {
        fin>>r>>t;
        /*register ull i;
        for(i=r;s<=t;i+=2,c++)
        {
            s+=(2*i+1);
        }
        */
        c = ((ull)(sqrt(8*t+(2*r-1)*(2*r-1))-(2*r-1)))>>2;
        fout<<"Case #"<<x+1<<": "<<c<<endl;
    }
    return 0;
}
