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
ofstream ouf("ti.out");
const int maxlongint=2147483647;

int i,j,k,t,n,m;
int zu,zz;
char dd[10][10];
string ss[5]={"","X won","O won","Draw","Game has not completed"};

bool chk(char x)
{
  int c1,c2,c3=0,c4=0,c5=0;
  for (i=1;i<=4;i++)
  {
    c1=c2=0;
    for (j=1;j<=4;j++)
    {
      if (dd[i][j]==x||dd[i][j]=='T')
        c1++;
      if (dd[j][i]==x||dd[j][i]=='T')
        c2++;
    }
    if (dd[i][i]==x||dd[i][i]=='T')
      c3++;
    if (dd[i][5-i]==x||dd[i][5-i]=='T')
      c4++;
    c5=max(c5,max(c1,c2));
  }
  if (c3==4||c4==4||c5==4)
    return true;
  else
    return false;
}
  
      
int main()
{
  freopen("ti.out","w",stdout);
  inf>>zu;
  for (zz=1;zz<=zu;zz++)
  {
    for (i=1;i<=4;i++)
      for (j=1;j<=4;j++)
        inf>>dd[i][j];
    k=0;
    if (chk('X'))
      k=1;
    if (chk('O'))
      k=2;
    if (!k)
    {
      k=3;
      for (i=1;i<=4;i++)
        for (j=1;j<=4;j++)
          if (dd[i][j]=='.')
            k=4;
    }
    pf("Case #%d: %s\n",zz,ss[k].c_str());
  }
  return 0;
}

