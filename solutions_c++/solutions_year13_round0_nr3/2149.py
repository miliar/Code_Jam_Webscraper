#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define SIZE 10000005

using namespace std;
typedef long long int ll;

int imos[SIZE];
int kt[20];

bool ok(ll a)
{
	int s;
	ll ten;
	for(ten=1,s=0;ten<=a;ten*=10,s++);
	ten/=10;s--;
	for(int i=s;i>=0;i--)
	{
		kt[i]=a/ten;
		a%=ten;
		ten/=10;
	}
	for(int i=0;i<=s;i++)
	{
		if(kt[i]!=kt[s-i]) return false;
	}return true;
}
void make()
{
	for(ll i=0;i<SIZE;i++)
	{
		if(ok(i)&&ok(i*i))
		{
			imos[i]++;
		}
	}
	for(int i=1;i<SIZE;i++)
	{
		imos[i]+=imos[i-1];
	}
}
int sum(int a,int b)
{
	return imos[b]-(a>0?imos[a-1]:0);
}
void solve()
{
	int a,b;
	scanf("%d %d",&a,&b);
	a=ceil(sqrt((double) a));
	b=floor(sqrt((double) b));
	printf("%d\n",sum(a,b));
	return;
}
void test()
{
	int n;
	while(scanf("%d",&n))
	{
		if(ok(n)) printf("YES\n");
		else printf("NO\n");
	}
}
int main()
{
	//test();
	make();
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}return 0;
}
