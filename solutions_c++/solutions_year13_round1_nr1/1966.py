#include <fstream>
#include <iostream>
#include <cmath>
#define rep(x,y,z) for (int x=y;x<=z;x++)
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
long  q,c;
long long r,t,a;

int main()
{
    fin>>q;
    rep(w,1,q)
    {
               fin>>r>>t;
               r++;
               while ((2*r-1)<=t)
               {
                     t-=(2*r-1);
                     c++;
                     r+=2;
                     }
               fout<<"Case #"<<w<<": "<<c<<"\n";
               c=0;
               }
}
