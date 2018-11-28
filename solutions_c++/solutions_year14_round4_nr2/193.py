#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,n,k,ans,cnt;
int a[100010];


int main()
{
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);

	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d",a+i);
		int p = 1, q = n;
		ans = 0;
		for (int c=1;c<=n;c++)
		{
			int k = p;
			for (int i=p;i<=q;i++) if (a[i]<a[k]) k = i;
			//printf(" %d %d %d\n",p,q,k);
			if (k-p < q-k)
			{
				int t = a[k];
				for (int i=k;i>p;i--) a[i] = a[i-1], ans++;
				a[p] = t;
				p++;
			}
			else {
				int t = a[k];
				for (int i=k;i<q;i++) a[i] = a[i+1], ans++;
				a[q] = t;
				q--;
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
