#include<iostream>
using namespace std;
int a[4];
int b[4];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int ii = 1; ii <= tt; ii++)
	{
		int r1, r2, t, ans;	
		scanf("%d", &r1);
		for(int i = 1; i <= 4; i++)
		{
			for(int j = 0; j < 4; j++)
			if(i == r1)
			{
				scanf("%d", &a[j]);
			}
			else
			{
				scanf("%d", &t);
			}
		}
		scanf("%d", &r2);
		for(int i = 1; i <= 4; i++)
		{
			for(int j = 0; j < 4; j++)
			if(i == r2)
			{
				scanf("%d", &b[j]);
			}
			else
			{
				scanf("%d", &t);
			}
		}
		t = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(a[i] == b[j])
				{
					t++;
					ans = a[i];
				}
		if(t == 0)
			printf("Case #%d: Volunteer cheated!\n", ii);
		else if (t == 1)
			printf("Case #%d: %d\n", ii, ans);
		else
			printf("Case #%d: Bad magician!\n", ii);
	}
	return 0;
}