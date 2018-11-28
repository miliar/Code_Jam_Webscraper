#include<stdio.h>
#include<string.h>
#include<queue>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<math.h>
#include<stack>
#include<sstream>
using namespace std;

#define MAXN 10000000

long long acc[MAXN+5];
char tmp[55];

bool isPal ( long long x )
{
	sprintf(tmp,"%lld",x);
	int sz=strlen(tmp);
	for(int i=0 ; i<sz/2 ; i++)
		if(tmp[i]!=tmp[sz-i-1])
			return 0;
	return 1;
}

bool check ( long long x )
{
	long long x2 = x*x ;
	if ( isPal(x) && isPal(x2) ) 
		return 1;
	return 0;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for(int i=1 ; i<=MAXN ; i++)
		acc[i]=acc[i-1]+check(i);
	int t;
	long long a , b ;
	scanf("%d",&t);
	for(int tc=1 ; tc<=t ; tc++)
	{
		scanf("%lld%lld",&a,&b);
		int endd=(int)floor((double)sqrt(b*1.));
		int stt=(int)ceil((double)sqrt(a*1.))-1;
		printf("Case #%d: %lld\n",tc,acc[endd]-acc[stt]);
	}
	//while(1);
}