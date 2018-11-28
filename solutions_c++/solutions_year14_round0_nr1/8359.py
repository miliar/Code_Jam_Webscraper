#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int k=1; k<=t; k++)
	{
		bool a[20];
		fill(a, a+20, false);
		int r, temp, cnt, ans;
		scanf("%d", &r);
		for(int i=1; i<5; i++)
		{
			for(int j=1; j<5; j++)
			{
				scanf("%d", &temp);
				if(r==i)
				{
					a[temp] = true;
				}
			}
		}
		scanf("%d", &r);
		cnt = 0;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				scanf("%d", &temp);
				if(r==i && a[temp])
				{
					cnt++;
					ans = temp;
				}
			}
		}
		printf("Case #%d: ",k);
		if(!cnt)	printf("Volunteer cheated!\n");
		else if(cnt==1)	printf("%d\n",ans);
		else printf("Bad magician!\n");
	}
	return 0;
}
