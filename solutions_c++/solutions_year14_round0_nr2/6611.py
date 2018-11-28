#include<bits/stdc++.h>
typedef long long int LL;
typedef unsigned long long int ULL;

#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 


#define SET(v, val) memset(v, val, sizeof(v))
#define mp(a,b)    make_pair(a,b)
#define pb(n)      push_back(n)
#define PI 3.14159265
#define F first
#define S second


template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }

using namespace std;

int main()
{
	int t,i=1;
	double c,f,x,r=2;
	cin>>t;
	while(t--)
	{
		cin>>c>>f>>x;
		double ans=0;
		r=2;
		while(1)
		{
			double a=ans+((1.0*c)/(r)) + (1.0*x/(r+f));
			double b=ans+(1.0*x /r);
			if(a<b)
			{
				ans=ans+(1.0*c)/(r);
				r+=f;
			}
			else
			{
				ans=b;
				break;
			}
		}
		printf("Case #%d: %.7f\n",i,ans);
		i++;
	}
	return 0;
}
