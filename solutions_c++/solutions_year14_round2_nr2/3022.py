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
long long int a,b,k,c;

int main()
{

    int T,n=0;
    freopen("B-small-attempt0.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  cin>>T;
  while(T--)
  {
     n++;
     c=0;
     cin>>a>>b>>k;
     for(int i=0;i<a;i++)
     {
         for(int j=0;j<b;j++)
         {
             int p=i&j;
             if(p<k)
             {
                c++;
             }
         }
     }
     printf("Case #%d: %lld\n",n,c);

  }
  return 0;
}

