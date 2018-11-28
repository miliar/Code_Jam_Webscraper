#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
bool palinbanabo(char str[])
{
int x = strlen(str)-1;
for(int i = 0; i <= x; i++)
{
if (str[i] == str[x-i])
{
continue;
}
else
{
return false;
}
}

return true;
}

int main()
{


    bool t,t1;
    long long a,b,n,m,l,test;
    freopen("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    scanf("%lld",&test);
    for(l=1;l<=test;l++)
    {

    scanf("%lld %lld",&a,&b);
    long long int a1=sqrt(a);
    long long int b1=sqrt(b);
    long count=0;
    for(long long int n=a1;n<=b1;n++)
    {

        char str[100]={0};
        char str1[100]={0};
        if(n*n<a||n*n>b)
        continue;
        m=n;
        sprintf(str,"%lld",m);
       t= palinbanabo(str);
       if(t==false)
       continue;
       m=n*n;
        sprintf(str1,"%lld",m);
          t1= palinbanabo(str1);
          if(t==true&&t1==true)
          count++;

      }
      printf("Case #%lld: %ld\n",l,count);
    }
   return 0;
   }
