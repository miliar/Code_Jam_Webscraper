#include<iostream>

using namespace std;

int solve(int row1[], int row2[]);
int find(int num, int row[]);

void main()
{
	int cases;
	cin >> cases;
	
	for(int c = 1; c <= cases; c++)
	{
		int row1Num, row2Num, row1[4], row2[4], dummy;	
		
		cin >> row1Num;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> dummy;
				
				if (i + 1 == row1Num)
				{
					row1[j] = dummy;					
				}
			}
		}
		
		cin >> row2Num;
		
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				cin >> dummy;
				
				if (i + 1 == row2Num)
				{
					row2[j] = dummy;					
				}
			}
		}
		
		int ans = solve(row1, row2);
		
		cout << "Case #" << c << ": ";
		
		switch(ans)
		{
		case -2:
			cout << "Bad magician!";
			break;
		case -1:
			cout << "Volunteer cheated!";
			break;
		default:
			cout << ans;
			break;
		}
		
		cout << endl;
	}
}

//-2 : Bad magician!
//-1 : Volunteer Cheated!
// Else: Response
int solve(int row1[], int row2[])
{
	int number = -1;
	
	for(int i = 0; i < 4; i++)
	{
		int curr = row2[i];
					
		if (find(curr, row1) != -1)
		{
			if (number != -1)
			{
				return -2;
			}
			
			number = curr;
		}
	}
	
	return number;
}

int find(int num, int row[])
{
	for(int i = 0; i < 4; i++)
	{
		if (row[i] == num)
		{
			return i;
		}
	}
	
	return -1;
}