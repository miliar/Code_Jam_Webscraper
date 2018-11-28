#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int lawn[105][105], maxR[105], maxC[105];

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	int t;
	scanf(" %d", &t);
	for(int k=1; k<=t; k++)
	{
		memset(maxR, 0, sizeof(maxR));
		memset(maxC, 0, sizeof(maxC));
		
		int n, m;
		scanf(" %d %d", &n, &m);
		
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
			{
				scanf(" %d", &lawn[i][j]);
				maxR[i] = max(maxR[i], lawn[i][j]);
				maxC[j] = max(maxC[j], lawn[i][j]);
			}
		
		bool isPossible = true;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				if(maxR[i] > lawn[i][j] && maxC[j] > lawn[i][j])
					isPossible = false;
		
		if(isPossible)
			printf("Case #%d: YES\n", k);
		else
			printf("Case #%d: NO\n", k);
	}
	return 0;
}
