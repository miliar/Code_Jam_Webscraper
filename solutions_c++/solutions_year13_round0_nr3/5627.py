#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int ispal(long long z)
{
  long long rr, x, p, digits[4];
  p=0;
  rr=z;
  while (z>0){++p; digits[p]=z%10; z=z/10;}
  for (x=1; x<=((p+1)/2);++x) if (digits[x]!=digits[p+1-x])return 0;
  return 1;
}

int main()
{
    long long i, t, r, k, n, a, b;
    fstream infile("C-small.in");
    ofstream outfile("C-small.out");
    infile >> t;
    for(i=1; i<=t; ++i)
    {
      infile >> a >> b;
      cout << a << ' ' << b <<' ' <<endl;      
      r=0;
      a=int(ceil(sqrt(a)));
      b=int(floor(sqrt(b)));cout<<a<<"..."<<b<<endl;
      for (k=a; k<=b; ++k) if (ispal(k)&&ispal(k*k)){++r; cout <<k<<","<<k*k<<endl;}
      outfile << "Case #" <<i<<": " <<r<<endl;
      cout << "Case #" <<i<<": " <<r<<endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
