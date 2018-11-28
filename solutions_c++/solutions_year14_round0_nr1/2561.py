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
	  int t1;
	  freopen("a.in","r",stdin);
	  freopen("2.out","w",stdout);
	  in(t1);
	  int r=1;
	  while(t1--)
	  {
	  	  map<int,int>m;
	  	  map<int,int>::iterator t;
	  	  int a,b;
	  	  in(a);
	  	  for(int i=1;i<=4;i++)
	  	  {
	  	  	   for(int j=1;j<=4;j++)
	  	  	   {
	  	  	   	     int y;
	  	  	   	     in(y);
	  	  	   	     if(i==a)
	  	  	   	       m[y]++;
	  	  	   }
	  	  }
	  	  in(b);
	  	  for(int i=1;i<=4;i++)
	  	  {
	  	  	   for(int j=1;j<=4;j++)
	  	  	   {
	  	  	   	     int y;
	  	  	   	     in(y);
	  	  	   	     if(i==b)
	  	  	   	       m[y]++;
	  	  	   }
	  	  }
	  	  printf("Case #%d: ",r);
	  	  if(m.size()==8)
	  	     printf("Volunteer cheated!\n");
	  	  else
	  	  {
	  	  	    int twos=0;
	  	  	    int ans=0;
	  	  	    for(t=m.begin();t!=m.end();t++)
	  	  	    {
	  	  	    	 if(t->second ==2)
	  	  	    	 {
	  	  	    	 	twos++;
	  	  	    	 	ans=t->first;
	  	  	    	 }
	  	  	    }
	  	  	    if(twos>=2)
	  	  	       printf("Bad magician!\n");
	  	  	    else
	  	  	    {
	  	  	    	printf("%d\n",ans);
	  	  	    }
	  	  }
	  	  r++;
	  }
	  return 0;
}
	
	
	
	
	
	
	
	
	
	
	

