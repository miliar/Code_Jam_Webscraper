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

/*inline int isSpaceChar(char c)
{
return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
}

inline int FAST_IO()
{
char ch;
int val=0;
ch=getchar_unlocked();
while(isSpaceChar(ch))
ch=getchar_unlocked();
val=0;
while(!isSpaceChar(ch))
{
val=(val*10)+(ch-'0');
ch=getchar_unlocked();
}
return val;
}*/
int a[5][5];
bool mark[20];
int main(void)
{
  int t,tc;
  scanf("%d",&tc);
  for(t=1;t<=tc;t++)
  {
    int p,i,j,c=0,r1,r2;
    scanf("%d",&r1);
    r1--;
    memset(mark,false,sizeof(mark));
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)
    scanf("%d",&a[i][j]);

    for(i=0;i<4;i++)
    mark[a[r1][i]]=true;
    scanf("%d",&r2);
    r2--;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)
    scanf("%d",&a[i][j]);
    for(i=0;i<4;i++)
    if(mark[a[r2][i]]==true)
    {
      c++;
      p=a[r2][i];
    }
    printf("Case #%d: ",t);
    if(c==1)
    {
      printf("%d\n",p);
    }
    else if(c>1)
    {
      printf("Bad magician!\n");
    }
    else if(c==0)
    {
       printf("Volunteer cheated!\n");
    }
  }
  return 0;
}




