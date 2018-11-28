/*
ID: mfs6174
email: mfs6174@gmail.com
PROG: ti
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<iomanip>
#include<cmath>
#include<set>
#define sf scanf
#define pf printf
#define llg long long 

using namespace std;
ifstream inf("ti.in");
//ofstream ouf("ti.out");
const int maxlongint=2147483647;

double c,f,x,tt,t,m;
int zu,zz;

int main()
{
  freopen("ti.out","w",stdout);
  inf>>zu;
  for (zz=1;zz<=zu;zz++)
  {
    inf>>c>>f>>x;
    m=2.0;
    tt=x/m;
    t=1e200;
    while (tt<t)
    {
      t=tt-x/m+c/m+x/(m+f);
      m+=f;
      double tmp=t;
      t=tt;
      tt=tmp;
    }
    pf("Case #%d: %.7lf\n",zz,t);
  }
  return 0;
}
