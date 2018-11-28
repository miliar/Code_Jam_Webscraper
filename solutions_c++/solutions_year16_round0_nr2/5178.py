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

string s;

int main()
{
	int n,i,t,l,c,tt=1;
	//freopen("C:/Users/NEW/Desktop/inp2.in","r",stdin);
	//freopen("C:/Users/NEW/Desktop/out2.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		c=0;
		cin>>s;
		s=s+'+';
		l=s.size();
		char t1=s[0];
		
		for(i=1;i<l;i++)
		{
			if(t1!=s[i])
			{
				c++;
				t1=s[i];
			}
		}
		printf("Case #%d: %d\n",tt,c);
		tt++;
	}
	return 0;
}