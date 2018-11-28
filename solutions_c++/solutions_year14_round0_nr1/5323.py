#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int T;
bool flag[20];

int main()
{
	freopen("magic.in","r",stdin);
	freopen("magic.out","w",stdout);
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		int L, last, cnt=0;
		scanf("%d",&L);
		memset(flag,0,sizeof flag);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				int x;
				scanf("%d",&x);
				if (i==L) flag[x]=true;
			}
		scanf("%d",&L);
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				int x;
				scanf("%d",&x);
				if (i==L && flag[x])
				{
					last=x;
					cnt++;
				}
			}
		if (!cnt)
			printf("Case #%d: Volunteer cheated!\n",TT);
		else
		if (cnt>1)
			printf("Case #%d: Bad magician!\n",TT);
		else
			printf("Case #%d: %d\n",TT,last);
	}
	return 0;
}

