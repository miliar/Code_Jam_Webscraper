#include <iostream>

using namespace std;

int main(void)
{
	int n;
	int row1;
	int arr1[4][4];
	int sol1[4];
	int row2;
	int arr2[4][4];
	int sol2[4];

	int matches;
	int solution;

	cin >> n;
	
	for(int i=0;i<n;i++)
	{
		matches = 0;

		cin >> row1;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				cin >> arr1[j][k];
		}
		
		for(int k=0;k<4;k++)
		{
			sol1[k] = arr1[row1-1][k];
		}

		cin >> row2;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				cin >> arr2[j][k];
		}

		for(int k=0;k<4;k++)
		{
			sol2[k] = arr2[row2-1][k];
		}

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(sol1[j]==sol2[k])
				{
					matches++;
					solution = sol1[j];
				}
			}
		}

		cout << "Case #" << i+1 << ": "; 
		if(matches==1)
			cout << solution << endl;	
		else if(matches>1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}

}
