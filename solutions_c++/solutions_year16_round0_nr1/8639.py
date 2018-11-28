#include <bits/stdc++.h>
#define pb push_back
#define fi first
#define sc second
#define inf 2000000000
#define MP make_pair
#define orta ((a+b)/2)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define dbg(x) cerr<<#x<<":"<<x<<endl
#define N 105
#define MOD 1000000007
using namespace std;
typedef  pair <int ,int> ii;
typedef  long long int lint;
int d[10],bay=0;
void add(lint k)
{
	while(k)
	{
		if(d[k%10]==0)
		{
			d[k%10]=1;
			bay--;
		}
		k=k/10;
	}
}
int main()
{
//	freopen("asdsada.in","r",stdin);
//	freopen("asdsada.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	for (int qqq = 0; qqq<ts ; qqq++)
	{
		memset(d,0,sizeof(d));
		long long int a,cev=0;
		bay=10;
		scanf("%lld",&a);
		if(a==0)
		{
			printf("Case #%d: INSOMNIA\n",qqq+1);
			continue;
		}
		while(bay)
		{
			cev+=a;
			add(cev);
		 }
		printf("Case #%d: %lld\n",qqq+1,cev);
	}
}




