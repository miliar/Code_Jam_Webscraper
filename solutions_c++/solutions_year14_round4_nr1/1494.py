#include <cstdio>

int dy[710];

int main ()
{
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
	int t,n,x,y,ans;
	scanf ("%d",&t);
	for (int g=1;g<=t;g++)
	{
		scanf ("%d %d",&n,&x);
		for (int i=0;i<710;i++)
			dy[i] = 0;
		ans = 0;
		for (int i=0;i<n;i++)
		{
			scanf ("%d",&y);
			dy[y]++;
		}
		for (int i=x;i>0;i--)
		{
			while (dy[i]>0)
			{
				int j = x-i;
				ans++;
				dy[i]--;
				while (dy[j]==0&&j>=0)
					j--;
				if (dy[j]!=0)
					dy[j]--;
			}
		}
		printf ("Case #%d: %d\n",g,ans);
	}
}
