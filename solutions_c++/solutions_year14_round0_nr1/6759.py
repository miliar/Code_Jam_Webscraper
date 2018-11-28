#include<iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int k=0; k<t; k++)
	{
		int row1, row2;
		int cards1[4][4], cards2[4][4];
		
		// First Round Values
		cin >> row1;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			cin >> cards1[i][j];
		}	
		
		// Second Round Values
		cin >> row2;
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			cin >> cards2[i][j];
		}
		
		// Card Matching
		int total = 0;
		bool matching[4]={false};
		for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			matching[i] |= (cards2[row2-1][j] == cards1[row1-1][i]);
			total += (cards2[row2-1][j] == cards1[row1-1][i]);
		}
		
		// Output Filtering
		cout << "Case #" << k+1 << ": ";
		if(total > 1)	cout << "Bad magician!\n";
		else if(total == 0) cout << "Volunteer cheated!\n";
		else
		{
			for(int j=0; j<4; j++)
				if(matching[j])	cout << cards1[row1-1][j] << endl;
		}
	}
	return 0;
}
