/*Mayoor Bishnoi*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>

#define inp(n) scanf("%d",&n);
#define inp2(x,y) scanf("%d%d",&x,&y);
#define inpl(n) scanf("%lld",&n);
#define inpl2(x,y) scanf("%lld%lld",&x,&y);
#define out(n) printf("%d\n",n);
#define outl(n) printf("%lld\n",n);
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORR(i,b,a) for(int i=b-1;i>=a;i--)
#define PB(a) push_back(a)
#define C(x) printf("%d\n",x);

using namespace std;

typedef vector< int > vi;
typedef pair< int,int > pii;
typedef vector< pii > vpii;
typedef list< int > li;
typedef long long ll;
typedef unsigned long long ull;

/*int gcd(int a,int b)
{
	while(b)
		b^=a^=b^=a%=b;
	return a;
}*/

/*int mypower(int base,int index)
{
	if(index == 0)
		return 1;
	else if(index == 1)
		return base;
	int temp=mypower(base,index/2);
	temp=(temp*temp);
	if(index&1)
		return temp*base;
	else
		return temp;
}*/

main()
{
	int t,m;
	int n[20],k[20],num=1,small,large;
	double x;
	inp(t)
	while(t--)
	{
		inp(m)
		int y=0,z=0;
		FOR(i,0,m)
		{
			scanf("%lf",&x);
			n[i]=x*(1000000);
		}
		sort(n,n+m);
		FOR(i,0,m)
		{
			scanf("%lf",&x);
			k[i]=x*(1000000);
		}
		sort(k,k+m);
		int l=0;
		/*FOR(i,0,m)
			if(n[0]<k[i])
				l++;*/
		int j=0,p;
		for(p=0;p<m;p++)
		{
			while(j<m)
			{
				if(n[p]>k[j])
					j++;
				else
					break;
			}
			if (j == m)	
				break;
			j++;
		}
		y=(m-p);
		l=0;
		FOR(i,0,m)
		{
			if(n[i]>k[l])
			{
				z++;
				l++;
			}
		}
		printf("Case #%d: %d %d\n",num++,z,y);
		
	}
	
	return 0;
}