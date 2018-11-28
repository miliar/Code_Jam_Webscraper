#include <cstdio>
#include <cstring>

using namespace std;

int test,cnt,a[4][4],b[4][4],h[20],n,m;
int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	scanf("%d",&test);
	while (test--)
	{
		cnt++;
		scanf("%d",&n);
		for (int i=0; i<4; i++)
		   for (int j=0; j<4; j++)
		   	  scanf("%d",&a[i][j]);	
		scanf("%d",&m);
		for (int i=0; i<4; i++)
		   for (int j=0; j<4; j++)
		   	  scanf("%d",&b[i][j]);
		memset(h,0,sizeof h);
		int tot=0,ans;
		for (int i=0; i<4; i++) h[a[n-1][i]]=1;
		for (int i=0; i<4; i++)
			if (h[b[m-1][i]]==1)
			{
				tot++;
				ans=b[m-1][i];
			}
		printf("Case #%d: ",cnt);
		if (tot==1) printf("%d\n",ans);
		else if (tot>1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	//while (1);
}
