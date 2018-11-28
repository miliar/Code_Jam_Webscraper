#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(ll n)
{
	ll t=0;
	if(n==0)
	{
		printf("INSOMNIA\n");
		return;
	}
	for(int i=1;;i++)
	{
		ll nt=n*i;
		while(nt>0) t|=1LL<<(nt%10),nt/=10;
		if(t==1023) {printf("%lld\n",n*i);return;}
	}
}

int n;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T,I=1,i,j;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		printf("Case #%d: ",I++);
		solve(n);
		cerr<<"Case #"<<I-1<<" done\n";
	}
	return 0;
}
