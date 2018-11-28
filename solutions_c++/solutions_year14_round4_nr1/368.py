#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
typedef pair<int,int> PII;

#define maxn 101010
#define maxe 202020

int a[maxn],n,x;
int main()
{
	int ncase,tt=0,i,j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		scanf("%d %d",&n,&x);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		int ans=0,cnt=0;
		for(i=0,j=n-1;;)
		{
			if(i!=j&&a[j]+a[i]<=x)
			{
				j--,i++;
				cnt+=2;
				ans++;
			}
			else
			{
				j--;
				cnt++;
				ans++;
			}
			if(cnt>=n)
				break;
		}
		printf("Case #%d: %d\n",++tt,ans);
	}
	return 0;
}