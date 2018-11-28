#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#define P printf
#define PN printf("\n");
#define PR(a) printf("%d",a);
#define PRN(a) printf("%d\n",a);

using namespace std;

#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define Set(a,c) memset(a, c, sizeof(a))
#define oo 1000000000
#define MAXN 100005
#define S(a) scanf("%d",&a);
#define SN(a) printf("%d\n",a);
int pal(const vector<char>& v )
{
  int i,j;
  for(i=0,j=v.size()-1;i<=j;j--,i++)
        if(v[i]!=v[j])rteurn 0;

  return 1;
}
int main ()
{
  	//freopen("small.in","rt",stdin);
	//freopen("hello.txt","wt",stdout);
	int i,j,t,n,m,x,y,no,save,r;
  long k;
  char a[51][51];
  char str1[1001][101],str2[1001][101];
  vector<char>u,v;
  scanf("%d",&t);int test=0;
  while(t--)
  {
      test++;int cnt=0;
      printf("Case #%d: ",test);

      scanf("%d %d",&n,&k);
      for(i=n;i<=k;i++)
      {
          v.clear();u.clear();
          if(sqrt(i)==ceil(double(sqrt(double(i)))))
          {
            j=i;
            while(j!=0)
            {
              v.pb(j%10);j/=10;
            }
           for(j=v.size()-1;j>=0;j--)
            u.pb(v[j]);

           for(j=0;j<v.size();j++)
            if(v[j]!=u[j])break;

           if(j==v.size()&&pal(v))cnt++;

          }
      }
printf("%d\n",cnt);
  }

 return 0;
}
