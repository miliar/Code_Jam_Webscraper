#include <stdio.h>
#include <set>
std::set<int> myset;
void doe(int x)
{
	long long n,k,i,gg;
	scanf("%lld",&gg);
	printf("Case #%d: ",x);
	if(gg==0)
	{
		printf("INSOMNIA\n");
		return;
	}
	n=0;
	while(myset.size()!=10)
	{
		k=n;
		while(k!=0)
		{
			myset.insert(k%10);
			k/=10;
		}
		n+=gg;
	}
	printf("%lld\n",n-gg);
	myset.clear();
}
int main()
{
	freopen("Ain.in","r",stdin);
	freopen("Aout.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		doe(i);
	return 0;
}
