#include <iostream>
#include <cstdio>
using namespace std;

int a[8][8], b[8][8];

int main()
{
	int test;
	int row1, row2;
	
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		cin >> row1;
		for(int i = 1; i <= 4; i ++)
			for(int j = 1; j <= 4; j ++)
				cin >> a[i][j];
		cin >> row2;
		for(int i = 1; i <= 4; i ++)
			for(int j = 1; j <= 4; j ++)
				cin >> b[i][j];
		
		int same = 0;
		int number = -1;
		for(int j = 1; j <= 4; j ++)
		{
			for(int k = 1; k <= 4; k ++)
				if(a[row1][j] == b[row2][k])
				{
					same ++;
					number = a[row1][j];
				}
		}
		
		if(same == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", cas);
		}
		else if(same == 1)
		{
			printf("Case #%d: %d\n", cas, number);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", cas);
		}
	}
	
	return 0;
}