#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int n,m,map[4][4],cnt[17];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.out","w",stdout);
	int test;
	scanf("%d",&test);
		for(int p = 0; p<test; p++)
		{
			int f;
			scanf("%d",&f);
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
					scanf("%d",&map[i][j]);
			}

			for(int i=0; i<4; i++)
				cnt[map[f-1][i]]++;
			int s;
			scanf("%d",&s);
			for(int i=0; i<4; i++)
			{
				for(int j=0; j<4; j++)
					scanf("%d",&map[i][j]);
			}
			for(int i=0; i<4; i++)
				cnt[map[s-1][i]]++;

			int two = 0;
			int v = 0;
			for(int i=1; i<17; i++)
			{
				if(cnt[i] == 2)
				{
					two++;
					v = i;
				}
			}
			
			if(two == 0)
			{
				printf("Case #%d: Volunteer cheated!\n",p+1);
			}
			if(two == 1)
			{
				printf("Case #%d: %d\n",p+1,v);
			}
			if(two > 1)
			{
				printf("Case #%d: Bad magician!\n",p+1);
			}

			for(int i=1; i<17; i++)
				cnt[i] = 0;
		}

return 0;
}