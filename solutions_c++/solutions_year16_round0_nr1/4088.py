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
#define md 1000000007 
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
int n,m,h[10];
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
int main()
{
  int i,j,k,l,t1,t2,t3,t4,t5,t6,t7,t8,t9,t,nw;
  int tt1,tt2,tt3,tt4;
  double u1,u2,u3,u4,u5,u6,u7,u8,u9;
  char c1,c2,c3;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  int T,T2,totMax=0,totMax2;
  /*
		for(i=1;i<=1000000;i++)
  {
  	
  	int cnt=0,maxChange=0;
  	for(j=0;j<10;j++)h[j]=0;
  	for(j=1;j<=1000;j++)
  	{
  		if (cnt==10)break;
  		t=i*j;
  		for(;t;)
  		{
  			if (h[t%10]==0)
					{
					 h[t%10]=1;cnt++;
					 if (j>=100)
					  system("pause");
					 maxChange=max(maxChange,j);
					}
  			t/=10;
  		}
  		
  	}
  //	cout<<i<<" : "<<maxChange<<endl;
  	totMax=max(maxChange,totMax);
  	if (maxChange == totMax) totMax2=i;
  	cout<<totMax2<<' '<<totMax<<endl;
  }
  cout<<totMax<<endl;
  */
		
  cin>>T;
  for(T2=1;T2<=T;T2++)
  {
  	printf("Case #%d: ",T2);
  	cin>>n;
  	if (n==0) {printf("INSOMNIA\n"); continue;}
  	
  	int cnt=0,maxCount=0;
  	for(j=0;j<10;j++)h[j]=0;
  	for(j=1;j<=1000;j++)
  	{
  		if (cnt==10)break;
  		t=n*j;
  		for(;t;)
  		{
  			if (h[t%10]==0)
					{
					 h[t%10]=1;cnt++;
					 maxCount = n*j;
					}
  			t/=10;
  		}
  		
  	}
  	printf("%d\n",maxCount);
  }
  return 0;
}
