#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
ifstream in ("input");
ofstream out ("output");
int main ()
{   int k,t,a,b,i,i2,i3,inv,np;
    in>>t;
    for(k=1;k<=t;k++)
    {
        np=0;
        in>>a>>b;
        for(i=a;i<=b;i++)
            {
                inv= 0;
                i2 = i;
                while (i2 != 0)
                {
                    inv = inv * 10 + i2 % 10;
                    i2 = i2 / 10;
                }
                i2=(int)sqrt(i);
                if (i == inv&&sqrt(i)==i2)
                {
                    i3=i2;
                    inv= 0;
                    i2 = i3;
                    while (i2 != 0)
                    {
                        inv = inv * 10 + i2 % 10;
                        i2 = i2 / 10;
                    }
                    if (i3 == inv)   np++;
                }
            }
        out<<"Case #"<<k<<": "<<np;
        if(k!=t) out<<endl;
    }
    return 0;
}

