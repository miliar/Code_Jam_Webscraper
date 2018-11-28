#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int count=1; count<=T; count++)
	{
		int r1, r2;
		int rows1[16][16], rows2[16][16];
		cin >> r1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin >> rows1[i][j];
		cin >> r2;
		
		int num;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> rows2[i][j];
			}
		}
		
		// Check
		int found = 0;
		for(int i=0; i<4; i++)
		{
			for(int k=0; k<4; k++)
			{
				if(rows1[r1-1][i] == rows2[r2-1][k])
				{
					found++;
					num = rows1[r1-1][i];
				}
			}
		}
		
		if(found == 0)	// No such element found
			cout << "Case #"<<count<<": Volunteer Cheated!" << endl;
		else if(found == 1)	// Just one element found
			cout << "Case #"<<count<<": " << num << endl;
		else if(found >= 2)	// More than one element found
			cout << "Case #"<<count<<": Bad Magician!" << endl;
	}
	return 0;
}
