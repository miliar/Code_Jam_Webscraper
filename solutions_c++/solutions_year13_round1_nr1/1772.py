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
#define LL long long
#define S(a) scanf("%d",&a);
#define SN(a) printf("%d\n",a);
	LL expo(long long a, int b){
	  long long result = 1;

	  while (b){
	    if (b%2==1){
	      result *= a;
	      //while(result>=1000000007)
		//result-=1000000007;
	    }
	    b =b>>1;
	    a *= a;
	//while(a>=1000000007)
	//a-=1000000007;  }
	  return result;	}}

int main ()
{
      freopen("in.txt","rt",stdin);
    freopen("hello.txt","wt",stdout);
	LL i,j,t,n,m,x,y,no,save,r;

  long k;
  char a[5][5],diag1[5],diag2[5];
  scanf("%d",&t);int test=0;
  while(t--)
  {
      LL x=0;
      int no=0;
      test++;
      LL co=0,ans=0;
      printf("Case #%d: ",test);

      cin>>r>>n;

      while(ans<=n)
      {
         ans+=2*(r+x)+1;
         co++;
         x+=2;
      }
cout<< co-1 <<"\n";
  }
 return 0;
}
