#include<iostream>
using namespace std;
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<stack>
#include<map>
#include<set>
#include<string.h>
#include<math.h>
#define MOD 1000000007
#define MIN -100000000
#define MAX 100000000
#define ll long long int
template<class T>T gcd(T a,T b){return (b==0)?a:gcd(b,a%b);}
template<class T>T lcm(T a,T b){return (a*b)/gcd(a,b);}
template<class T>T powmod(T a,T b) {T res=1;for(;b;b>>=1){if(b&1)res=res*a;a=a*a;}return res;}

/* HOPE n WILL :)
	NGU :)
	_/\_ 	*/
// MG

int a[131075];
ll divi(ll num)
{
		ll kk=2;
				while(kk*kk<=num)
				{
					if(num%kk==0)
					{
						return kk;
					}
					kk++;
				}
				return 0;
}
int main()
{
	int n,t;
	ll i,j;
	for(i=2;i<65540;i+=2)
	a[i]=0;
	for(i=3;i<=65540;i+=2) //   0 prime
	{								// 	 1 non-prime
		if(a[i]==0)
		{
			for(j=i*i;j<=65540;j=j+2*i)
			{
				if(a[j]==0)
				a[j]=i;
			}
		}
	}
	int jj,tt=1;
	scanf("%d",&t);
	int x,c=0,ct=0;
	while(t--)
	{
		scanf("%d %d",&n,&jj);
		printf("Case #%d:\n",tt);
		tt++;
		for(i=32769;i<=65535;i+=2)
		{
			if(a[i]!=0)
			{
				x=i;
				c=0;
				int base2[33];
				while(x!=0)
				{
					base2[c++]=x%2;
					x=x/2;
				}
				ll k;
				
				k=0;
				ll base3,base4,base5,base6,base7,base8,base9,base10;
				base3=base4=base5=base6=base7=base8=base9=base10=0;
				for(k=0;k<c;k++)
				{
					if(base2[k]==1)
					{
						base3=base3+powmod(3ll,k);
						base4=base4+powmod(4ll,k);
						base5=base5+powmod(5ll,k);
						base6=base6+powmod(6ll,k);
						base7=base7+powmod(7ll,k);
						base8=base8+powmod(8ll,k);
						base9=base9+powmod(9ll,k);
						base10=base10+powmod(10ll,k);
					}
				}
				if(divi(base3)==0 || divi(base4)==0 || divi(base5)==0 || divi(base6)==0 || divi(base7)==0 || divi(base8)==0 || divi(base9)==0 || divi(base10)==0)
				continue;
				ct++;
				for(k=c-1;k>=0;k--)
				printf("%d",base2[k]);
				cout<<" ";
				cout<<a[i];
				cout<<" ";
				printf("%lld %lld %lld %lld %lld %lld %lld %lld\n",divi(base3),divi(base4),divi(base5),divi(base6),divi(base7),divi(base8),divi(base9),divi(base10));
				if(ct==jj) 
				break;
			}
		}
	}
	return 0;
}