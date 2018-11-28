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
template<class T>T powmod(T a,T b,T mod) {T res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}

/* HOPE n WILL :)
	NGU :)
	_/\_ 	*/
// MG

set<int> s;
int main()
{
	int n,i,t,tt=1;
	//freopen("C:/Users/NEW/Desktop/inp11.in","r",stdin);
	//freopen("C:/Users/NEW/Desktop/out1.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",tt);
			tt++;
			continue;
		}
		int nn=n;
		int c=2;
		while(1)
		{
			int num=nn;
			while(num>0)		
			{
				s.insert(num%10);
				num=num/10;
			}
			if(s.size()==10)
			{
				printf("Case #%d: %d\n",tt,nn);
				tt++;
				s.clear();
				break;
			}
			nn=n*c;
			c++;
		}
	}
	return 0;
}
