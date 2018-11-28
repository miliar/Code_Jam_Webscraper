#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

#define LL long long

LL ans[1048576],l,r;
int s=0;
int a[20];
int t=0;
int T;

bool check(LL num)
{
	for (t=0;num>0;num/=10) a[t++]=num%10;
	for (int i=0;i+i<=t;i++) if (a[i]!=a[t-i-1]) return false;
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    for (LL i=1;i<=10000000;i++)
		if (check(i) && check(i*i))
			ans[++s]=i*i;
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++)
	{
		printf("Case #%d: ",ww);
		scanf("%I64d%I64d",&l,&r);
		int as=0;
		for (int i=1;i<=s;i++)
			if (ans[i]>=l && ans[i]<=r) as++;
		printf("%d\n",as);
	}
    return 0;
}
