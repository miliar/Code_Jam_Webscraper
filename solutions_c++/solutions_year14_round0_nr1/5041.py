#include <iostream>
using namespace std;

int main()
{
	int times;
	cin >> times;
	int arr[4][4];
	int arr2[4][4];
	int n;
	int count=0;
	int val;
	int time2=0;
	int row1, row2;
	while(times > 0)
	{
		count=0;
		time2++;
		cin >> row1;
		row1 -=1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> arr[i][j];
			}
		}
		cin >> row2;
		row2 -=1;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> arr2[i][j];
			}
		}

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[row1][i] == arr2[row2][j])
				{
					count++;
					val = arr[row1][i];
				}
			}
		}

		cout << "Case #" << time2 << ": ";
		if(count == 1)
		{
			cout << val << endl;
		}
		if(count > 1)
		{
			cout << "Bad magician!" << endl;
		}
		if(count == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		times--;
	}
}