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
//freopen("ti.in","r",stdin);
const int maxlongint=2147483647;

int i,j,k,n,m,zu,zz;
int dd[5][5][5];
int main()
{
  inf>>zu;
  for (zz=1;zz<=zu;zz++)
  {
    inf>>n;
    for (int i=1;i<=4;i++)
      for (int j=1;j<=4;j++)
        inf>>dd[1][i][j];
    inf>>m;
    for (int i=1;i<=4;i++)
      for (int j=1;j<=4;j++)
        inf>>dd[2][i][j];
    int rt=0;
    for (int i=1;i<=4;i++)
      for (int j=1;j<=4;j++)
        if (dd[1][n][i]==dd[2][m][j])
        {
          if (!rt)
            rt=dd[1][n][i];
          else
            rt=-1;
        }
    if (rt==-1)
    {
      ouf<<"Case #"<<zz<<": Bad magician!"<<endl;
      continue;
    }
    if (rt==0)
    {
      ouf<<"Case #"<<zz<<": Volunteer cheated!"<<endl;
      continue;
    }
    ouf<<"Case #"<<zz<<": "<<rt<<endl;
  }
  return 0;
}
