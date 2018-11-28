#include <cstdio>
#include <iostream>

using namespace std;


int T,a[4][4],b[4][4],ans1,ans2,c[17],kol,ans;

int main()
{
#ifndef ONLINE_JUDGE
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);
#endif
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		kol = 0;
		for (int j = 0; j < 17; j++)
			c[j] = 0;

		cin >> ans1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				cin >> a[j][k];
				if (j+1 == ans1) c[a[j][k]]++;
			}

		cin >> ans2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				cin >> b[j][k];
				if (j+1 == ans2 && c[b[j][k]]) 
				{
					kol++;
					ans = b[j][k];
				}
			}
		
		if (kol == 0) 
			printf("Case #%d: Volunteer cheated!\n", i);
		else 
			if (kol == 1) 
				printf("Case #%d: %d\n", i, ans);
			else 
			printf("Case #%d: Bad magician!\n", i);
		

	}
	return 0;
}