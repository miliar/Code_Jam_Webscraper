#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

typedef long long ll;
ll aa,bb;

bool ok(ll k)
{
	int m[20],num=0;
	while(k)
	{
		m[num++]=k%10;
		k/=10;
	}
	for(int i=0;i<num/2;++i)
		if(m[i]!=m[num-1-i])
			return false;
	return true;
}

int work()
{
	int sum=0;
	ll a=sqrt(aa),b=sqrt(bb);
	if(a*a<aa)
		++a;
	for(ll i=a;i<=b;++i)
		if(ok(i) && ok(i*i))
			++sum;
	return sum;
}

int main ()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;++ii)
	{
		scanf("%lld%lld",&aa,&bb);
		printf("Case #%d: %d\n",ii,work());
	}
	return 0;
}
