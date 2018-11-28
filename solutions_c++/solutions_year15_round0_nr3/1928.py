// powered by xpd1  /i love shimokawa_mikuni and i haven't touch my devc for 3 months. 
// All of these left only broken history after 12.4.22. sacrifice for my  love.
// on 2012-10-
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
LL gcd(LL x,LL y){LL t;for(;y!=0;){t=x%y;x=y;y=t;}return x;}
int L,X,a[10005],pref[10005],suf[10005],tmp[10005];
char s[10005];
int dy[8][8];
int changeSign(int x){if (x>3)return x-4;else return x+4;}
int main()
{
  int i,j,k,l,t1,t2,t3,t4,t5,t6,t7,t8,t9,t,nw,smax;
  int tt1,tt2,tt3,tt4,ans;
  double u1,u2,u3,u4,u5,u6,u7,u8,u9;
  char c1,c2,c3;
  int yuzhi=10;
  srand((unsigned)time(0));//srand(72888306);
  #ifndef ONLINE_JUDGE
  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
  #endif
  int T,T2;
  // 0:1 1:i 2:j 3:k 4:-1 5:-i 6:-j 7:-k
  dy[0][0]=0;dy[0][1]=1;dy[0][2]=2;dy[0][3]=3;
  dy[1][0]=1;dy[1][1]=4;dy[1][2]=3;dy[1][3]=6;
  dy[2][0]=2;dy[2][1]=7;dy[2][2]=4;dy[2][3]=1;
  dy[3][0]=3;dy[3][1]=2;dy[3][2]=5;dy[3][3]=4;
  for(i=0;i<=7;i++)
   for(j=0;j<=7;j++)
   {
   	if (i<=3&&j<=3)continue;
   	if (i<=3&&j>3)
   	{
   		dy[i][j]=changeSign(dy[i][j-4]);
   	}
   	else if (i>3&&j<=3)
   	 dy[i][j]=changeSign(dy[i-4][j]);
   	else 
   	 dy[i][j]=dy[i-4][j-4];
   }
		cin>>T;
  for(T2=1;T2<=T;T2++)
  {
  	cout<<"Case #"<<T2<<": ";
  	cin>>L>>X;
  	cin>>s;
  	for(i=1;i<=L;i++)a[i]=(s[i-1]=='i'?1:(s[i-1]=='j'?2:3));
  	pref[0]=0;
  	for(i=1;i<=L;i++)pref[i]=dy[pref[i-1]][a[i]];
			suf[L+1]=0;
  	for(i=L;i>=1;i--)suf[i]=dy[a[i]][suf[i+1]];
  	for(i=0;i<=yuzhi;i++)
  	{
  		for(j=1;j<=L;j++)
  		{
  			if (i==0)tmp[j]=pref[j];
  			else tmp[j]=dy[pref[L]][tmp[j]];
  			if (tmp[j]==1)
  			{break;}
  		}
  		if (j<=L) break;
  		
  	}
   if (i>yuzhi)
   {cout<<"NO"<<endl;continue;}
   t1=i;t2=j;
   for(i=0;i<=yuzhi;i++)
  	{
  		for(j=L;j>=1;j--)
  		{
  			if (i==0)tmp[j]=suf[j];
  			else tmp[j]=dy[tmp[j]][suf[1]];
  			if (tmp[j]==3)
  			{break;}
  		}
  		if (j>=1) break;
  		
  	}
  	if (i>yuzhi)
   {cout<<"NO"<<endl;continue;}
   t3=i;t4=j;
   
   if (t3+t1+1+(t2>=t4)>X)
   {cout<<"NO"<<endl;continue;}
   if (t2<t4&&t3+t1+1==X)
   {
   	t1=0;
   	for(i=t2+1;i<=t4-1;i++)
   	 t1=dy[t1][a[i]];
   	cout<<(t1==2?"YES":"NO")<<endl;continue;
   }
   if (X-t3-t1-2<0)
    ts=0;
   
   t5=suf[t2+1];
   for(i=1;i<=(X-t3-t1-2)%8;i++)
    t5=dy[t5][pref[L]];
   t5=dy[t5][pref[t4-1]];	
   cout<<(t5==2?"YES":"NO")<<endl;continue;
  }
  return 0;
}

