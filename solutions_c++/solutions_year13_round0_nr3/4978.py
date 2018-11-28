#include<iostream>
#include<cstring>
#include<string>

using namespace std;

const int maxn=10000;
int nume,ca,numa,x,y,num;
int e[maxn],a[maxn];
bool check(long long x)
{
	int nume=0;
	while (x!=0)
	{
		e[++nume]=x%10;
		x/=10;
	}

	for (int i=1; i<=nume/2; i++)
		if (e[i]!=e[nume-i+1]) return false;

	return true;
}
void prepare()
{
	for (int i=0; i<=10000000; i++)
	{
		long long tmp1=i, tmp2=tmp1*tmp1;
		if (check(tmp1) && check(tmp2))	a[++numa]=tmp2;	 
	}
}
void init()
{
	prepare();
	cin>>num;
	while (num--)
	{
		cin>>x>>y;
		int ans=0;
		for (int i=1; i<=numa; i++)
			if ((a[i]>=x) && (a[i]<=y)) ++ans;
		printf("Case #%d: %d\n",++ca,ans);
	}
}
int main()
{
	freopen("ccc.in","r",stdin);
	freopen("ccc.out","w",stdout);
	init();
	return 0;
}
