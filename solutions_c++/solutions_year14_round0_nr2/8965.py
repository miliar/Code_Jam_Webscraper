#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdlib>

using namespace std;

#define S(n) scanf("%d",&n)
#define P(n) printf("%d\n",n)
#define SS(str) scanf("%s",str)
#define PS(str) printf("%s\n",str)
#define SLL(n) scanf("%lld",&n)
#define PLL(n) printf("%lld\n",n)
#define PB(n) push_back(n)
#define MP(a,b) make_pair(a,b)
#define rep(i,n) for(i=0;i<n;i++)
#define rep1(i,n) for(i=1;i<=n;i++)
#define rep2(i,a,b) for(i=a;i<b;i++)
#define LL long long
#define MOD 1000000007LL
#define sortt(v) sort(v.begin(),v.end())
#define pii pair<int,int>
#define SZ(v) v.size()
#define blank printf("\n")

#define sieve(a) ({int b=ceil(sqrt(a));vector<int> d(a,0);vector<int> e;int f=2;e.push_back(2);e.push_back(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.push_back(c);}}e;})

int main()
{
	int i,j,k,l,m,n,t,u;
	double c,f,x,time=0,cookie=0,t1,t2,rate1,cookie1,t3,pre,farmtime,rate;

	S(t);
	rep(u,t)
	{
		scanf("%lf%lf%lf",&c,&f,&x);

		pre = (x*1.0)/2.0;
		i = 1;
		time = 0;
		farmtime = 0;
		rate = 2.0;
		while(1)
		{
			t2 = (c*1.0)/rate;
			farmtime += t2;
			rate1 = 2.0 + (i)*f;
			t3 = (x*1.0)/rate1;

			if(pre < farmtime + t3)
			{
				time = pre;
				break;
			}
			else
			{
				pre = farmtime + t3;
				rate = rate1;
			}
			i++;
		}	
		printf("Case #%d: %.7lf\n",u+1,time);
	}

	return 0;
}
