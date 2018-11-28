#include <iostream>

using namespace std;

void magic(int test, int row1, int row2, int * m, int * m2)
{
	int count = 0;
	int num = 0;
	for(int i = 0; i < 4 ;i++)
	{
		for(int j = 0; j < 4 ; j++)
		{
			if( m[i+(4*(row1-1)) ] == m2[j +(4*(row2-1))])
			{
				count++;
				num = m[i+(4*(row1-1))];
			}
		}
	}
	if(count == 1)
	{
		cout << "CASE #" << test << ": " << num << endl;
	}
	if( count > 1)
	{
		cout << "CASE #" << test << ": Bad magician!" << endl;
	}
	if( count < 1)
	{
		cout << "CASE #" << test << ": Volunteer cheated!" << endl;
	}
	return;
}

int main()
{
	int tests, row1, row2;
	int matrix[16] = {0};
	int matrix2[16] ={0};
	int temp = 0;
	cin >> tests;
	for(int i = 0; i < tests; i++)
	{
		cin >> row1;
		for(int j = 0; j < 16; j++)
		{
			cin >> temp;
			matrix[j] = temp;
		}
		cin >> row2;
		for(int j = 0; j< 16; j++)
		{
			cin >> temp;
			matrix2[j] = temp;
		}
		
	  magic(i+1, row1, row2, matrix, matrix2);
		
	}
	
	return 0;
}
