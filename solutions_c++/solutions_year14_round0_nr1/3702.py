#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
	
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("output.ou", "w", stdout);
	int T; scanf("%d", &T);
	
	for (int ii=0; ii<T; ii++) {
		int a; scanf("%d", &a);
		
		vector<int> v = vector<int>();
		
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				if (i==a-1)
				{
					int x; scanf("%d", &x);
					v.push_back(x);
				}
				
		scanf("%d", &a);
		
		int res = 0;
		int cnt = 0;
		for (int i=0; i<4; i++)		
			for (int j=0; j<4; j++)
				if (i==a-1)
				{
					int x; scanf("%d", &x);
					for (int k=0; k<4; k++)
					{
						if (v[k] == x)
						{
							res = x;
							cnt++;
						} 
					}
				}
				
		if (cnt == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", ii);
		}
		
		if (cnt == 1)
		{
			printf("Case #%d: %d\n", ii, res);
		}
		
		if (cnt > 1)
		{
			printf("Case #%d: Bad magician!\n", ii);
		}
	}
	return 0;
}