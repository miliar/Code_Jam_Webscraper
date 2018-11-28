#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
#include<climits>
#include<set>
#include<cmath>
#include<bitset>
#include<map>
#include<iostream>
#include<queue>
#define test(t) while(t--)
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%llu",&n)
 
#define p(n) printf("%llu\n",n)
#define rep(i,a,n) for(i=a;i<=n;i++)
#define vi vector<int>
#define vii vector< vector<int> >
#define vpii vector< pair<int,int> >
#define mii map<int,int>
#define pb push_back
#define inf 1000000000LL
#define mp make_pair
#define MOD 1000000009LL
#define ll long long
#define gc getchar_unlocked
using namespace std;
int main()
{
int t,n,i,j,k,l;
double a[1005],tmp,b[1005];
int ans1,ans2;
s(t);
for(l=1;l<=t;++l)
{
	ans1=ans2=0;
	s(n);
	for(i=1;i<=n;++i)
	scanf("%lf",&a[i]);
	for(i=1;i<=n;++i)
	scanf("%lf",&b[i]);
	for(i=1;i<=n;++i)
	{
		for(j=1;j<i;++j)
		{
			if(a[j]-a[i]>0.0)
			{
				tmp=a[j];
				a[j]=a[i];
				a[i]=tmp;
			}
		}
	}
	for(i=1;i<=n;++i)
	{
		for(j=1;j<i;++j)
		{
			if(b[j]-b[i]>0.0)
			{
				tmp=b[j];
				b[j]=b[i];
				b[i]=tmp;
			}
		}
	}
	i=n;j=1,k=n;
	while(i>=1 && j<=n && k>=1)
	{
		if(a[i]-b[k]>0.0)
		{
		ans2++;
		i--;
		j++;
	    }
	    else
	    {
	    	i--;
	    	k--;
	    }
	    
	}
	i=1;j=1;
	while(i<=n && j<=n)
	{
		if(a[i]-b[j]>0.0)
		{
		ans1++;
		i++;
		j++;
	    }
	    else
	    i++;
	}
	printf("Case #%d: %d %d\n",l,ans1,ans2);
}

return 0;
}
