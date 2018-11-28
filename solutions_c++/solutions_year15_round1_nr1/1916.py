//by Tanmay Chaudhari
#include <bits/stdc++.h>

using namespace std;

#define si(a)				scanf("%d",&a)
#define sl(a)				scanf("%lld",&a)
#define sd(a)				scanf("%lf",&a)
#define ss(a)				scanf("%s",a)
#define pi(a)				printf("%d\n",a)
#define pl(a)				printf("%lld\n",a)
#define LL				    long long 
#define pb(x)				push_back(x)
#define mp(x,y)				make_pair(x,y)
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<ii>			vii;
typedef vector<vii>			vvii;
#define MAX	1000005
#define all(a)				a.begin(),a.end()
#define allrev(a)			a.rbegin(),a.rend()			
#define forall(i,a,b)		for(int i=a; i<b; i++)
#define forrev(i,a,b)		for(int i=a; i>=b; i--)
#define w(t)				int t;si(t);while(t--)
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define bit(x,i)					(x&(1<<i))  //select the bit of position i of x
#define lowbit(x)					((x)&((x)^((x)-1))) //get the lowest bit of x
#define hBit(msb,n)					asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x
/*long long fast_exp(int base, int exp)
{
	long long res = 1;
	while (exp>0)
	{
		if (exp&1==1)
			res = (res*base) % MOD;
		base = (base*base) % MOD;
		exp /= 2;
	}
	return res%MOD;
}*/
long long arr[MAX];
long long ans, temp,maxm,minm;
int main()
{
	int t,n,m;
	si(t);
	for(int tt=1;tt<=t;tt++)
	{
		printf("Case #%d: ",tt);
		si(n);
		for(int i=0;i<n;i++)
			sl(arr[i]);
		maxm=minm=0;
		for(int i=0;i<n-1;i++)
			if(arr[i]>=arr[i+1])
				minm+=(arr[i]-arr[i+1]);
		printf("%lld ",minm);
		maxm=LLONG_MIN;
		ans=0;
		for(int i=1;i<n;i++)
			maxm=max(maxm,arr[i-1]-arr[i]);
		for(int i=0;i<n-1;i++)
		{
			if(arr[i]>=maxm)
				ans+=maxm;
			else
				ans+=arr[i];
		}
		printf("%lld\n",ans);
	}
	return 0;
}
