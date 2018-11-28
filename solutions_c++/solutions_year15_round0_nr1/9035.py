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


int main()
{
  freopen("ti.out","w",stdout);
  int zz,zu;
  inf>>zu;
  for (zz=1;zz<=zu;zz++)
  {
    int sm;
    inf>>sm;
    string ss;
    inf>>ss;
    int mc=0,ac=0;
    mc+=ss[0]-'0';
    for (int i=1;i<ss.size();i++)
    {
      if (mc<i)
      {
        ac+=i-mc;
        mc+=i-mc;
      }
      mc+=ss[i]-'0';
    }
    printf("Case #%d: %d\n",zz,ac);
  }
  return 0;
}
