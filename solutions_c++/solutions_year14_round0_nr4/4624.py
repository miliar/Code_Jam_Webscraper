#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int test,n,cnt;
double a[1111],b[1111];
int h[1111];
int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	scanf("%d",&test);
	while (test--)
	{
		cnt++;
		printf("Case #%d: ",cnt);
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%lf",a+i);
		for (int i=0; i<n; i++) scanf("%lf",b+i);
		sort(a,a+n);
		sort(b,b+n);
		//for (int i=0; i<n; i++) printf("%lf ",b[i]);
		//printf("\n");
		int l=0,r=n-1,ans=0;
		for (int i=n-1; i>=0; i--)
		{
			if (b[i]>a[r])
			{
				l++;
			} else
			{
				r--;
				ans++;
			}
		}
		printf("%d ",ans);
		ans=0;
		memset(h,0,sizeof h);
		for (int i=0; i<n; i++)
		{
		  bool flag=false;
		  for (int j=0; j<n; j++)
		    if (h[j]==0 && b[j]>a[i])
		    {
				h[j]=1;
				flag=true;
				break;
			}
		  if (!flag)
		  {
				ans++;
				for (int j=0; j<n; j++)
				if (h[j]==0)
				{
					h[j]=1;
					break;
				}
		  }
		}
		printf("%d\n",ans);		
	}
	//while (1);
}
