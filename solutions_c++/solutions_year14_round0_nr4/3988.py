#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;


int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
   long long n,x1=1;
   scanf("%d",&n);
   while(n>0)
   {
       long k,c1=0,c2=0;
       double g,b;
       scanf("%d",&k);
       vector<double> v1;
       vector<double> v2;
       vector<double> v3;
       vector<double> v4;
       FOR(i,0,k)
       {
          scanf("%lf",&g);
          v1.push_back(g);
       }
       FOR(j,0,k)
       {
          scanf("%lf",&b);
          v2.push_back(b);
       }
       sort(v1.begin(),v1.end());
       sort(v2.begin(),v2.end());
       int i1=0;
       FOR(x,0,v1.size())
       {
           if(v1[x]>v2[i1])
           {
               c1++;
               i1++;
           }
       }
       int i2=0;
       FOR(y,0,v2.size())
       {
           if(v2[y]>v1[i2])
           {
               c2++;
               i2++;
           }
       }
       cout<<"Case #"<<x1<<": "<<c1<<" "<<v2.size()-c2<<endl;
    n--;
    x1++;
   }

}

