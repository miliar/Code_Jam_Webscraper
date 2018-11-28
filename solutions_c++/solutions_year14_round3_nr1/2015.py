#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
char a[4];
long long int p,q;
int m,n=0;
int main()
{


   freopen("A-small-attempt1.in", "r", stdin);
 freopen("out1.txt", "w", stdout);

  scanf("%d",&m);

  while(m!=0)
  {
      m--;
     n++;
     scanf("%lld%c%lld",&p,&a[0],&q);
     int t=q;
     int test=1,coun=0;
     while(t>2&&t!=p)
     {
         t=t/2;
         if(t%2!=0&&t!=p)
            {test=0;break;}
     }
     if(test==0)
     {
         printf("Case #%d: impossible\n",n);
     }
     else if(p<q)
     {
         while(p<q&&coun<=40)
         {
             q=q/2;
             t=q;
             coun++;
             if(p<q)
             {


             while(1)
             {
                 if(t<=p)
                   {p=t;break;}
                 else
                    t=t/2;
             }
             }

         }
         if(coun<=40)
         printf("Case #%d: %d\n",n,coun);
         else
          printf("Case #%d: impossible\n",n);
     }
     else if(p>=q)
        printf("Case #%d: 1\n",n);
  }
  return 0;
}
