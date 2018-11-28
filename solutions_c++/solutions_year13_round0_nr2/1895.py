#include <iostream>
using namespace std;

int table[100][100];
int cur[100][100];

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int k = 0; k < n; k++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		for (int i = 0; i < a; i++)
			for (int s = 0; s < b; s++)	
			{
				scanf("%d", &table[i][s]);
				cur[i][s] = 100;
			}


		bool h = true;
		for (int x = 99; x > 0; x--)
		{
			for (int i = 0; i < a; i++)
			{
				int cnt = 0;
				for (int s = 0; s < b; s++)
				{
					if (table[i][s] > x)
						break;     
					cnt++;
				}                        
				if (cnt == b)
					for (int s = 0; s < b; s++)
						cur[i][s] = x;
			}
			for (int i = 0; i < b; i++)
			{
				int cnt = 0;
				for (int s = 0; s < a; s++)
				{
					if (table[s][i] > x)
						break;        
					cnt++;
				}
				if (cnt == a)
					for (int s = 0; s < a; s++)
						cur[s][i] = x;
			}
			for (int i = 0; i < a; i++)
				for (int s = 0; s < b; s++)
				{
					if (table[i][s] <= x && cur[i][s] != x)
						h = false;
				}                          
		}
		printf("Case #%d: %s\n", k + 1, (h == true ? "YES" : "NO"));
	}

	return 0;
}