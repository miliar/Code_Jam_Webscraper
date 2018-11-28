#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int cases;
	vector<int> results;
	cin >> cases;
	for(int i = 0; i < cases; i++)
	{
		int row1, row2;
		cin >> row1;
		int numbers1[4], useless[4];
		for(int j = 0;j<4;j++)
		{
			if(j+1 == row1)
			{
				cin >> numbers1[0];
				cin >> numbers1[1];
				cin >> numbers1[2];
				cin >> numbers1[3];
			}
			else
			{
				cin >> useless[0];
				cin >> useless[1];
				cin >> useless[2];
				cin >> useless[3];	
			}
		}
		cin >> row2;
		int numbers2[4];
		for(int k = 0;k<4;k++)
		{
			if(k+1 == row2)
			{
				cin >> numbers2[0];
				cin >> numbers2[1];
				cin >> numbers2[2];
				cin >> numbers2[3];
			}
			else
			{
				cin >> useless[0];
				cin >> useless[1];
				cin >> useless[2];
				cin >> useless[3];
			}
		}
		for(int a = 0;a < 4; a++)
		{
			for(int b = 0; b < 4; b++)
			{
				if(numbers1[a] == numbers2[b])
				{
					results.push_back(numbers1[a]);
				}
			}
		}
		cout << "Case #" ;
		if(results.size()==0)
		{
			 cout << i+1 << ": Volunteer cheated!" << endl; 
		}
		else if(results.size()==1)
		{
			cout << i+1 << ": " << results[0] << endl;
		}
		else
		{
			cout << i+1 << ": Bad magician!" << endl;
		}
		for(int y = 0;y < 4; y++)
		{
			numbers1[y] = 0;
			numbers2[y] = 0;
		}
		results.clear();
	} 
	return 0;
}
