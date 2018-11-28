#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <cassert>
#include <valarray>
#include <cmath>
#include <time.h>
#include <stack>
#include <queue>
#include <vector>
#define mood 1000000007
#define rep(a,n) for(LL i=a;i<=n;i++)
#define rep0(n) for(LL i=0;i<n;i++)
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
#define sqr(x) ((x)*(x))
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);
typedef long L;
typedef long long LL;
typedef unsigned long long ULL;
typedef std::map <L,L> MapType;
typedef std::map<std::string,std::string> Mappy;
using namespace std;
bool comp(pair<int,int> x,pair<int,int> y)
{
    return x.first < y.first ;
}
int main()
{
   freopen("jamin1.txt","r",stdin);
   freopen("jamout1.txt","w",stdout);
   int t;
   cin>>t;
   for(int i=1;i<=t;i++)
   {
      int r1,r2;
      int xx[17]={0};
      cin>>r1;
      int a[4][4],b[4][4];
      for(int p=0;p<4;p++)
        for(int q=0;q<4;q++)
             cin>>a[p][q];
      cin>>r2;
      for(int p=0;p<4;p++)
        for(int q=0;q<4;q++)
             cin>>b[p][q];
      int c=0,x=0;
      for(int j=0;j<4;j++)
      {
         xx[a[r1-1][j]]++;
         xx[b[r2-1][j]]++;
      }

       for(int j=1;j<=16;j++)
       {
           if(xx[j]==2)
           {
               c++;
               x = j;
           }
       }
      if(c==1)
          printf("Case #%d: %d\n",i,x);
      else if(c>=2)
          printf("Case #%d: Bad magician!\n",i);
      else if(c==0)
          printf("Case #%d: Volunteer cheated!\n",i);
   }
}

