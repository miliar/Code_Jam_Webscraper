#include<cstdio>
#include<vector>

using namespace std;

int y(vector<int> p)
{
	int n = p.size();
	int ret=0;
	for(int i = 1; i < n; i++)
		if(p[i]<p[i-1])
			ret+=p[i-1]-p[i];
	return ret;
}

int z(vector<int> p)
{
	int n = p.size();
	int speed=0;
	for(int i = 1; i < n; i++)
	{
		if(p[i-1]-p[i]>speed)
			speed=p[i-1]-p[i];
	}
	int ret=0;
	for(int i = 0; i < n-1; i++)
	{
		if(p[i]<=speed) ret+=p[i];
		else ret+=speed;
	}
	return ret;
}

void solve()
{
	int n;
	scanf("%d",&n);
	vector<int> p(n);
	for(int i = 0; i < n; i++)
		scanf("%d",&p[i]);
	printf(" %d %d\n",y(p),z(p));
}

int main()
{
	int ncases;
	scanf("%d",&ncases);
	for(int i = 1; i <= ncases; i++)
	{
		printf("Case #%d:",i);
		solve();
	}
	return 0;
}
