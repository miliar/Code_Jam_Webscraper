#include <iostream>
#include <fstream>

#define sf(x) scanf("%d",&x);

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output1.txt","w",stdout);

	int T;
	int a;
	int b;

	int x[4][4];
	int y[4][4];
	int temp;

	sf(T);

	for(int t=1;t<=T;t++)
	{
		sf(a);
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				sf(x[m][n]);
			}
		}

		sf(b);

		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				sf(y[m][n]);
			}
		}

		int ans1 = 0;
		int ans2;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(x[a-1][i] == y[b-1][j])
				{
					ans1 ++;
					ans2 = x[a-1][i];
				}
			}
		}

		
		if(ans1 == 1)
		{
			printf("Case #%d: %d\n",t,ans2);
		}
		else if(ans1 == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",t);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",t);
		}

	}
}