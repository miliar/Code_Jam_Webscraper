#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<time.h>
using namespace std;
//wahaha wahahaha

int n, m;
int a[10009];
int b[10009];
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t;
	int tv;
	scanf("%d",&t);
	for(tv=0;tv<t;tv++)
	{
		scanf("%d %d",&n,&m);
		int i, j, k;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		int cnt=0;
		for(i=0;i<n;i++)
			b[i] = 0;
		for(i=n-1;i>=0;i--)
		{
			if(b[i] == 0)
			{
				b[i] = 1;
				j = m - a[i];
				k = upper_bound(a,a+n,j) - a;
				if(k>0)
				{
					k--;
					while(k>=0 && b[k] == 1)
						k--;
					if(k>=0)
					{
						b[k] = 1;
					}
				}
				cnt++;
			}
		}
		printf("Case #%d: %d\n",tv+1,cnt);
	}
}