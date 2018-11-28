/*logic ------------

*/
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<stack>
#include<stdio.h>
#include<queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define in(x) scanf("%d",&x)
#define inll(x) scanf("%lld", &x)
#define MOD 1000000007 // 10**9 + 7
#define INF 1e9
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define For(i, a, b) for (int i = a; i < b; i++)
#define Rfor(i, b, a) for (int i = b; i > a; i--)
#define all(v) v.begin(), v.end()
typedef long long ll;
typedef long l;

using namespace std;
const double pi = acos(-1.0);

/*
inline void fast(int &x)
{
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;

    for(;((c<48 || c>57) && c != '-');
    c = getchar_unlocked());

    if(c=='-')
    {
        neg = 1;
        c = getchar_unlocked();
    }

    for(; c>47 && c<58 ; c = getchar_unlocked())
    {
        x =(x<<1)+(x<<3) + c - 48;
    }

    if(neg)
        x = -x;
}

void op(int x)
{
    if(x<0)
    {
         putchar('-');
         x=-x;
    }
    int len=0,data[20];
    while(x)
    {
        data[len++]=x%10;
        x/=10;
    }
    if(!len)
       data[len++]=0;
    while(len--)
        putchar(data[len]+48);
    putchar('\n');
} */

int main()
{
        int t;
        freopen("b.in","r",stdin);
        freopen("b.out","w",stdout);
        int r=1;
        in(t);
        while(t--)
        {
        	  double c,f,x;
        	  scanf("%lf%lf%lf",&c,&f,&x);
        	  double res=x/2.0;
        	  double temp=0.0;
        	  double cnt=2.0;
        	  while(1)
        	  {
        	  	  temp+=c/cnt;
        	  	  cnt+=f;
        	  	  double ss = temp+x/cnt;
        	  	  if(ss<res)
        	  	     res=ss;
        	  	  else
        	  	     break;
        	 }
        	 printf("Case #%d: ",r);
        	 printf("%.7lf\n",res);
        	 r++;
        }
        return 0;
}
	
	 

