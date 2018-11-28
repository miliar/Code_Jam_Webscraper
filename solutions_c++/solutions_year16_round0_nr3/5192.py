#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
typedef long long LL;
LL n,tot,a[10000];
const LL p[]={2,3,5,7,11,13,17,19,23,29};
LL check(LL x) {
	for (int i=0;i<10&&p[i]<x;i++)
		if (x%p[i]==0)return p[i];
	return 0;
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>n;puts("Case #1:");
	cin>>n>>tot;
	for(LL i=1;i<(1ll<<n)-1;i++)
	{
		if((i&1)==0||((i>>(n-1))&1)==0)continue;
		bool flag=1;
		for(LL j=2;j<=10;j++)
		{
			LL tp=0;
			for(LL k=n-1;k>=0;k--)tp=tp*j+((i>>k)&1);
			a[int(j)]=check(tp);
			if((a[int(j)])==0){flag=0;break;}
		}
		if(flag)
		{
			--tot;
			for(LL k=n-1;k>=0;--k)putchar(((i>>k)&1)?'1':'0');
			for(int j=2;j<=10;j++)printf(" %d",int(a[j]));
			puts("");
		}
		if(!tot)break;
	}
	if(tot>0)while(1);
	return 0;
}