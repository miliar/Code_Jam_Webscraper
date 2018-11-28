#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN=1010;
int a[MAXN];
int main()
{
	int t,n,i,j,flag=1;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int mmax=-1;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			mmax=max(mmax,a[i]);
		}
		int ans=mmax;
		for(i=1;i<=mmax;i++)
		{
			int temp=0;
			for(j=0;j<n;j++)
			{
				temp+=a[j]/i;
				if(a[j]%i==0)
					temp--;
			}
			temp+=i;
			ans=min(ans,temp);
		}
		printf("Case #%d: %d\n",flag++,ans);
	}
	return 0;
}
