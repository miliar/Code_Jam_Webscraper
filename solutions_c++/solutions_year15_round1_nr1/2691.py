#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define mp make_pair
#define pb push_back
#define sc(n) scanf("%d",&n)
#define pr(n) printf("%d\n",n)
#define sllc(n) scanf("%lld",&n)
#define pllc(n) printf("%lld\n",n)
#define MOD 1000000007
#define FOR(i,n) for(int i=0;i<n;i++)
int main()
{
	int t;
	sc(t);
	FOR(i,t)
	{
		int n,m[1002],max=0,diff,res1=0,res2=0;
		sc(n);
		FOR(j,n)
			sc(m[j]);
		printf("Case #%d: ",i+1);
		FOR(j,n-1)
		{
			if(m[j]>m[j+1])
			{
				res1+=m[j]-m[j+1];
				max=max>(m[j]-m[j+1])?max:(m[j]-m[j+1]);
			}
		}
		FOR(i,n-1)
		{
			if(m[i]<max)
			{
				res2+=m[i];
				//diff=0;
			}
			else
			{
				res2+=max;
				//diff=m[i]-max;
			}
		}
		printf("%d %d\n",res1,res2);
	}
	return 0;
}

