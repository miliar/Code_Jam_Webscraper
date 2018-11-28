#include <iostream>

using namespace std;

unsigned int findMatch(unsigned int * row1, unsigned int * row2, unsigned int * pos)
{
	unsigned int x=4;
	unsigned int y;
	unsigned result=0;
	while(x--)
	{
		y=4;
		while(y--)
		{
			if(row1[x]==row2[y])
			{
				result++;
				*pos = row1[x];
			}
		}
	}
	return result;
		
}

int main()
{
	unsigned int T;
	unsigned int i,j;
	unsigned int a,b;
	unsigned int row1[4];
	unsigned int row2[4];
	unsigned int row[4];
	unsigned int pos;
	unsigned int result;
	cin >> T;

	for (i=1;i<=T;i++)
	{
		cin >> a;
		for (j = 1; j <= 4; j++)
		{
			cin >> row[0] >> row[1] >> row[2] >> row[3];
			if (j == a)
			{
				row1[0]=row[0];
				row1[1]=row[1];
				row1[2]=row[2];
				row1[3]=row[3];
			}
		}
		cin >> b;
		for (j = 1; j <= 4; j++)
		{
			cin >> row[0] >> row[1] >> row[2] >> row[3];
			if (j == b)
			{
				row2[0]=row[0];
				row2[1]=row[1];
				row2[2]=row[2];
				row2[3]=row[3];
			}
		}
		cout << "Case #" << i << ": ";
		result = findMatch (row1, row2, &pos);
		if (result == 1)
			cout << pos;
		else if (result > 1)
			cout << "Bad magician!";
		else
			cout << "Volunteer cheated!";
		cout << endl;
	}
	
	return 0; 	
}
