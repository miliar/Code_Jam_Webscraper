#include <cstdio>
#include <cstring>
#include <cmath>
#define MAXN 1002
using namespace std;

// Counters
int cnt[MAXN];

// Pancakes
int pan[MAXN];

// Main
int main(void)
{
	int tc, cs, i, j, n, tmp, ans, cst, mx, plus, siz;

	// Read Input
	scanf("%d",&tc);
	for(cs=1;cs<=tc;cs++)
	{
		scanf("%d",&n);
		mx=0;
		memset(cnt,0,sizeof(cnt));
		for(i=0;i<n;i++)
		{
			scanf("%d",&pan[i]);
			if(pan[i]>mx) mx=pan[i];
			cnt[pan[i]]++;
		}
		ans=mx;

		// Greedy
		cst=0;
		for(i=1000;i>2;i--)
		{
			if(cnt[i])
			{
				cnt[i/2]+=cnt[i];
				cnt[(i+1)/2]+=cnt[i];
				for(j=i-1;j>=1;j--)
					if(cnt[j]) break;
				if(cst+cnt[i]+j<ans) ans=cst+cnt[i]+j;
				cst+=cnt[i];
			}
		}

		// Greedy
		cst=0;
		memset(cnt,0,sizeof(cnt));
		for(i=0;i<n;i++) cnt[pan[i]]++;
		for(i=1000;i>3;i--)
		{
			if(cnt[i])
			{
				siz=(int)sqrt(i);
				if(siz*siz==i)
				{
					cnt[siz]+=siz*cnt[i];
				}
				else
				{
					cnt[i/2]+=cnt[i];
					cnt[(i+1)/2]+=cnt[i];
				}
				for(j=i-1;j>=1;j--)
					if(cnt[j]) break;
				if(siz*siz==i)
				{
					if(cst+(siz-1)*cnt[i]+j<ans) ans=cst+(siz-1)*cnt[i]+j;
					cst+=(siz-1)*cnt[i];
				}
				else
				{
					if(cst+cnt[i]+j<ans) ans=cst+cnt[i]+j;
					cst+=cnt[i];
				}
			}
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}