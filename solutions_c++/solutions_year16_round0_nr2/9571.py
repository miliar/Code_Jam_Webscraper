#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)	
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define ss(n) scanf("%s",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)	for(i=a;i>=b;i--)
# define toint(n)	(n-'0')
typedef long long ll;

int main(int argc, char const *argv[])
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int len,t,k,i;
	ll n,ans,cnt;

	char s[101];

	s(t);
	fo(k,1,t+1)
	{

		ss(s);
		len= strlen(s);

		cnt=0;
		fo(i,0,len-1) {
			if(s[i]!=s[i+1]) {
				cnt++;
			}
		}

		if(s[len-1]=='-')
			cnt++;

		printf("Case #%d: %ld\n",k,cnt);
	}
	return 0;
}