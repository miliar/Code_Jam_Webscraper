#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
int n,i,j,k,x,y,t,rez;
long long a,b;
long long v[100005];

bool palindrom(long long w)
{
	int q[16];
	int p=0;
	while (w)
		p++,q[p]=w%10,w/=10;
	for (j=1;j<=p/2;j++)
		if (q[j]!=q[p+1-j]) return false;
	return true;
}

int main()
{
	//freopen("fair.in","r",stdin);
	//freopen("fair.out","w",stdout);
	scanf("%d",&t);
	for (int l=1;l<=t;l++)
	{
		rez=0;
		scanf("%lld %lld",&a,&b);
		x=int(sqrt(a));
		y=int(sqrt(b));
		for (i=x;i<=y && i*i<=b;i++)
			if (palindrom(i) && palindrom(i*i) && i*i>=a && i*i<=b) rez++;
		printf("Case #%d: %d\n",l,rez);
	}
	return 0;
}