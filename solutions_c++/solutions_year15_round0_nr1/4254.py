#include <iostream>
#include <algorithm>
#define ll long long int
#include <fstream>
#define val(x) ((int)(x - 48))
using namespace std;
ifstream in("input.in");
ofstream out("output.out");
int main()
{
  int t,i,j;
  char v[1003];
  ll s,nr,Smax;
  in >> t;
  for(i = 1 ; i <= t ; i ++)
  {
      s =  nr = 0;
      in >> Smax;
      in >> v;
      s = val(v[0]);
      for(j = 1 ; j <= Smax ; j++)
         if (val(v[j]))
            if (s<j)
         {
             nr +=j-s;
             s += j-s+val(v[j]);
         }
         else
            s += val(v[j]);
      out<<"Case #"<<i<<": "<<nr<<"\n";
  }
    return 0;
}
