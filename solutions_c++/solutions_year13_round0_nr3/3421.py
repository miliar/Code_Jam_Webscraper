#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define LL unsigned long long
#define ff first
#define ss second
#define PB push_back
#define MP make_pair
using namespace std;
LL t,n;
LL tab[]={1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002,
10000001,
10011001,
10100101,
10111101,
11000011,
11011011,
11100111,
11111111,
20000002};
LL a,b,poc,kon;
int main()
{
 for(int i=0;i<48;i++)
 tab[i]*=tab[i];
 scanf("%d",&t);
  for(int z=1;z<=t;z++)
  {
    printf("Case #%d: ",z);
    
    scanf("%d%d",&a,&b);
   
    for(int i=0;i<48;i++)
    {
      if(tab[i]>=a)
      {
	poc=i;
	break;
      }
    }
    for(int i=0;i<48;i++)
    {
      if(tab[i]>b)
      {
	kon=i;
	break;
      }
    }
    
    printf("%d\n",kon-poc);
  }
 
  
}