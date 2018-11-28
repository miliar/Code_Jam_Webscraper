#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
ifstream fin("B-large.in");
ofstream fout("file3334.txt");
long double c,f,x,p;
int T,k;
long int n;
fin>>T;
for(k=1;k<=T;k++)
{
    p=0;
    fin>>c>>f>>x;
    if(x<=c) p=x/2;
    else
    {
     for(n=0;n<=10000000;n++)
        {
            if(c>(x*f/(2+(n+1)*f)))
            {
                if(n==0) {p=x/2; n=10000001;}
                else
                {
                    for(int j=0;j<n;j++)
                    {
                        p=p+c/(j*f+2);
                    }
                 p=p+x/(n*f+2);
                 n=10000001;
                }
            }
        }
    }
    fout<<"Case #"<<k<<": ";
    fout<<fixed<<setprecision(7)<<p<<endl;
}
  return 0;
}