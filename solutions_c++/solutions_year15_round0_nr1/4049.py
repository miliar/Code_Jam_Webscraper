#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)	
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)	for(i=a;i>=b;i--)
# define toint(n)	(n-'0')
typedef long long ll;

int main(int argc, char const *argv[])
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t,k,i,smax;
	long total,friends;
	char s[1002];

	s(t);
	fo(k,1,t+1)
	{
		total=friends=0;

		s(smax);
		scanf("%s",s);

		fo(i,0,smax+1)
		{
			if((total<i)&&(toint(s[i])!=0)){
				friends+=(i-total);
				total+=(i-total);
			}
			total+=toint(s[i]);
		}

		printf("Case #%d: %ld\n",k,friends);
	}
	return 0;
}