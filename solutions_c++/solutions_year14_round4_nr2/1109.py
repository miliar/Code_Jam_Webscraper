#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iostream>
#include<cstring>
#define N 20
#define oo 0x3f3f3f3f
using namespace std;

int a[N],b[N],p[N];

bool check(int n)
{
	for(int i=0;i<n;i++)
    {
		bool flag=true;
		for(int j=0;j<i-1;j++)
			if(b[j]>b[j+1])
			{
				flag=false;
				break;
			}

		for(int j=i;j<n-1;j++)
			if(b[j]<b[j+1])
			{
				flag=false;
				break;
			}

		if(flag)
            return true;
	}

	return false;
}

int calc(int n)
{
	int res=0;
	for(int i=1;i<n;i++)
		for(int j=0;j<i;j++)
			if(p[j]>p[i])
				res++;
	return res;
}

int main(void)
{
	int t,n,ys=0;

    freopen("B-small-attempt0.in","r",stdin);
    freopen("testB.out","w",stdout);

	scanf("%d",&t);
	while(t--)
    {
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);

		for(int i=0;i<n;i++)
			p[i]=i;

		int ans=1000000;
		do{
			for(int i=0;i<n;i++)
				b[p[i]]=a[i];
			if(check(n))
				ans=min(ans,calc(n));

		}
		while(next_permutation(p,p+n));

		printf("Case #%d: %d\n", ++ys,ans);
	}

	return 0;
}
