#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>
using namespace std;
long long rev(unsigned long long int x)
{
     unsigned long long int r=0,d;
     while(x>0)
     {
               d=x%10;
               r=r*10+d;
               x=x/10;
     }
     return r;
}

bool pal(unsigned long long int x)
{
     long long y=rev(x);
     if(x==y)
     return 1;
     return 0;
}
int main()
{

     int t,k=0,cases=0,c1,c2;
     unsigned long long int j,ar[1000],a,b;
     freopen("C-small-attempt0.in","r",stdin);
     freopen("c.txt","w",stdout);//100000000000001
     for(unsigned long long int i=1;i<1001;i++)
     {
             if(pal(i))
             {

                                j=i*i;
                                if(pal(j))
                                ar[k++]=j;

             }
     }

     scanf("%d",&t);
     while(t--)
     {
               cases++;
               printf("Case #%d: ",cases);
               scanf("%llu%llu",&a,&b);
               if(a>ar[k-1])
               {printf("0\n");continue;}
               if(b>ar[k-1])
               b=ar[k-1];
               for(int i=0;i<k;i++)
               {
                       if(ar[i]>=a)
                       {c1=i;
                       break;}
               }
               for(int i=0;i<k;i++)
               {
                       if(ar[i]<=b)
                       c2=i;
               }
               printf("%d\n",c2-c1+1);

     }
}
