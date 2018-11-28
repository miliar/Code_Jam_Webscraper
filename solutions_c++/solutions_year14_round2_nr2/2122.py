// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define p(n)                        printf("%d",n)
#define pc(n)                       printf("%c",n)
#define pl(n)                       printf("%lld",n)
#define pln(n)                      printf("%lld\n",n)
#define pf(n)                       printf("%lf",n)
#define ps(n)                       printf("%s",n)
#define pn(n)                       printf("%d\n",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<=b;i++)
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
//Header Files
#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<string.h>
#include<algorithm>
#include<map>
typedef long long int ll;
using namespace std;

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

ll t;
cin>>t;
forall(z,1,t)
{
	ll a,b,k,count=0;
	sl(a);sl(b);sl(k);
	
	forall(i,0,a-1)
	{
		forall(j,0,b-1)
		{
			if((i&j)<k)
			count++;
		}
	}
	cout<<"Case #"<<z<<": "<<count<<endl;
	
}




	return 0;
}


