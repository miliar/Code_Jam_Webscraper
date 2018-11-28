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

int i,j,k,t,n,m;
int zz,zu;
int dd[110][110];
int h[110],l[100];

int main()
{
  freopen("ti.out","w",stdout);
  inf>>zu;
  for (zz=1;zz<=zu;zz++)
  {
    inf>>n>>m;
    for (i=1;i<=n;i++)
      for (j=1;j<=m;j++)
        inf>>dd[i][j];
    memset(h,0,sizeof(h));
    memset(l,0,sizeof(l));
    for (i=1;i<=n;i++)
      for (j=1;j<=m;j++)
        h[i]=max(h[i],dd[i][j]);
    for (i=1;i<=m;i++)
      for (j=1;j<=n;j++)
        l[i]=max(l[i],dd[j][i]);
    bool flag=true;
    for (i=1;i<=n;i++)
      for (j=1;j<=m;j++)
        if (dd[i][j]<h[i]&&dd[i][j]<l[j])
          flag=false;
    if (flag)
      pf("Case #%d: YES\n",zz);
    else
      pf("Case #%d: NO\n",zz);
  }
  return 0;
}
    
  
