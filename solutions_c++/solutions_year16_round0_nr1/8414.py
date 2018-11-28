#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define ull unsigned long long 
#define m(a,i,n) memset(a,i,n)
#define f(i,n) for(i=0;i<n;i++)
#define sc(a) scanf("%lld",&a)
#define vect_int vector<int>
#define pb(x) push_back(x)
#define lb lower_bound
#define ub upper_bound
#define pf(a) printf("%lld\n",a)
/*inline void Scan_f(int& a)
{
	char c = 0;
	while(c<33)
	c= getc(stdin);
	a = 0;
	while(c>33)
	{
		a = a*10 + c - '0';
		c = getc(stdin);
	}
}*//*
ll gcd(ll a,ll b)
{
	if(b == 0)
	{
	    return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}*/
//map<pair<ll,ll>,ll>  :: iterator itr;
//M[make_pair(a,b)]++;
int main() { 
	// your code goes here
 	ios_base::sync_with_stdio(false);
 	ll t,n,i,cnt,j,tmp;
 	sc(t);
 	bool a[10];
 	
 	for(i=1;i<=t;i++)
 	{ 	
 		sc(n);
 		cnt=0;
 		f(j,10)
 		a[j]=false;
 		if(n==0)
 		{
 			printf("Case #%lld: INSOMNIA\n",i);
		}
		else
		{
			for(j=0;;j++)
			{
				tmp=n*j;
				while(tmp>0)
				{
					if(a[tmp%10]==false)
					{
						cnt++;
						a[tmp%10]=true;
					}
					tmp/=10;
				}
				if(cnt==10)
				{
					tmp=n*j;
					printf("Case #%lld: %lld\n",i,tmp);
					break;
				}
			}
		}
 	}
	return 0;
}
