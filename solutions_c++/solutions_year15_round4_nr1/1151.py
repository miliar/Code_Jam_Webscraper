#include "cstdio"
#include "cstring"
#include "string"
#include "cmath"
#include "vector"
#include "set"
#include "utility"
#include "algorithm"

using namespace std;

int main(void)
{
	char arrow[5];
	int movei[5], movej[5];

	arrow[0] = '^';
	arrow[1] = '>';
	arrow[2] = 'v';
	arrow[3] = '<';

	movei[0] = -1;
	movei[1] = 0;
	movei[2] = 1;
	movei[3] = 0;

	movej[0] = 0;
	movej[1] = 1;
	movej[2] = 0;
	movej[3] = -1;

	int t;
	scanf("%d", &t);

	for(int test=1;test<=t;test++)
	{
		char input[102][102];
		int n,m;

		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++)
			scanf("%s", input[i]);

		bool possible = true;
		int ans = 0;
		for(int i=0;i<n;i++)
		{
			if(!possible) break;
			for(int j=0;j<m;j++)
			{
				if(!possible) break;
				if(input[i][j] == '.') continue;

				bool ok, able;
				able = false;
				ok = false;

				for(int k=0;k<4;k++)
				{
					int curri = i;
					int currj = j;

					curri += movei[k];
					currj += movej[k];

					while(curri>=0 && curri<n && currj>=0 && currj<m)
					{
						if(input[curri][currj] != '.')
						{
							able = true;
							ok |= (arrow[k] == input[i][j]);
							break;
						}	

						curri += movei[k];
						currj += movej[k];
					}
				}

				if(!able)possible = false;
				else ans += !ok;
			}
		}

		if(!possible) printf("Case #%d: IMPOSSIBLE\n", test);
		else printf("Case #%d: %d\n", test, ans);
	}
}

