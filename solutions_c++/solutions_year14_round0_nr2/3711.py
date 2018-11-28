/*
   nitesh kumar (codeshaker)
*/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <climits>
#include <complex>
typedef long long LL;
using namespace std;
int main(void)
{
int tc;
scanf("%d",&tc);
int i;
for(i=1;i<=tc;i++)
{
  double c,x,f;
  scanf("%lf%lf%lf",&c,&f,&x);
  double r=2.0,t1=0.0,t2=0.0,t=0.0;
  for(r=2.0;;r+=f)
  {
    t1=x/r;
    t2=(c/r)+(x/(r+f));
    if(fdim(t1,t2)==0)
    break;
    t+=(c/r);
  }
  t+=t1;
  printf("Case #%d: ",i);
  printf("%.7lf\n",t);
  }
  return 0;
  }
  /*
  4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0



Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

*/
