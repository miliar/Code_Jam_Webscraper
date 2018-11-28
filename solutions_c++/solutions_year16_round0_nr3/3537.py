// powered by xpd1  /i love shimokawa_mikuni and i haven't touch my devc for 3 months. 
// All of these left only broken history after 12.4.22. sacrifice for my  love.
// on 2016-04-09 
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <memory>
#include <fstream>
#include <string>
#include <utility>
#include <iomanip>
#define oo 2000000000
#define ol 200000000000000000ll
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <set>
//#include <conio.h>
#define oo 2000000000
#define ol 200000000000000000ll //=2E17
#define ooo 1E14
#define EPS 1E-10
#define mp make_pair
#define pb push_back
#define eps EPS
#define mem(x,y) (memset((x),y,sizeof((x))))
#define debug(x) cout << #x<<" = "<<x<<endl;
#ifdef __int64
 #define fmt64 "%I64d"
#else 
 #define fmt64 "%lld"
#endif
#define fi first
#define se second
using namespace std;
using namespace rel_ops;
const double PI=acos((double)-1);
typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
int ts,ts2,ts3,ts4;
int n,J,m,h[10];
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
char s[105];
int A[5]={2,3,5,7,61};
LL MOD(LL x,LL y,LL md)
{
	 return ((x*y-((LL)((double)x*y/md))*md)%md+md)%md;
}
LL powerMod(LL x,LL p,LL md)
{
	 LL t1=1,t2=x,ans=1;
	 for(;p;t2=MOD(t2,t2,md),t1++)
	 {
	 	if (p&(1ll<<t1))
	 	{
	 		ans=MOD(ans,t2,md);
	 		p-= (1ll<<t1);
	 	}
	 }
	 return ans;
}
int MillerRabin(LL x)
{
	 int i;
	 for(i=0;i<5;i++)
	 {
	 	if (powerMod(A[i],x-1,x)==1)return 1;
	 }
	 return 0;
}
LL PollardRho(LL n, LL c)  
{  
    LL i = 1, k = 2;  
    LL x = rand() % (n - 1) + 1;  
    LL y = x;  
    int cnt=0;
    while(1)  
    {  
        i++;  
        x = (MOD(x, x, n) + c) % n;  
        LL d = gcd((y - x + n) % n, n);  
        if(1 < d && d < n) {return d;}  
        if(y == x) return n;  
        if(i == k)  
        {  
            y = x;  
            k <<= 1;  
        }  
    }  
}  
LL certif[15];
int main()
{
  LL i,j,k,l,t1,t2,t3,t4,t5,t6,t7,t8,t9,t,nw;
  int tt1,tt2,tt3,tt4;
  double u1,u2,u3,u4,u5,u6,u7,u8,u9;
  char c1,c2,c3;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  int T,T2;
  cin>>T;
  for(T2=1;T2<=T;T2++)
  {
  	cin >>n>>J;
  	int cnt=0;
  	printf("Case #%d:\n",T2);
  	for(i=(1<<15)+1;i<1<<16;i+=2)
  	{
  		for(j=2;j<=10;j++)
  		{
  			t1=0;t2=1;
  			for(k=0;k<16;k++)
  			{
  				t1 += ((i>>k)&1)*t2;
  				t2*=j;
  			}
  		 if (MillerRabin(t1))
  		  break;
  		 else
					{
					 
				 }
				}
  		if (j>10)
  		{
  			for(j=2;j<=10;j++)
	  		{
	  			t1=0;t2=1;
	  			for(k=0;k<16;k++)
	  			{
	  				t1 += ((i>>k)&1)*t2;
	  				t2*=j;
	  			}
	  			
  			 LL p=t1,c=120;
						while(p >= t1) p = PollardRho(t1, c--);  
						certif[j]=p;
						cerr<<i<<endl;
					}
  	 	for(k=15;k>=0;k--)
  	 	 cout<<((i&(1<<k))? 1:0);
  	 	for(k=2;k<=10;k++)
  	 	 printf(" %I64d",certif[k]); 
  	  cout<<endl;
  	  cnt++;
  	  if (cnt>=J)
  	   break;
				}
			//	cerr<<i<<endl;
			}
  }
  return 0;
}
