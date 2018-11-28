#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int c,ans,ans1;
	int arr[4][4],arr2[4][4];
	ifstream file("A-small-attempt2.in", ios::in);
	ofstream ofile("task.txt", ios::out);

	file >> c;
	for (int k = 0; k < c; k++)
	{

		file >> ans;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				file >> arr[i][j];
			}
		};
		file >> ans1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				file >> arr2[i][j];
			}
		};
		int count = 0, card;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (arr[ans - 1][i] == arr2[ans1 - 1][j])
				{
					card = arr[ans - 1][i];
					count++;

				}
			}
		}

		if (count == 1)
		{
			ofile << "Case #" << k + 1 << ": " << card << endl;
		}
		else if (count > 1)
		{
			ofile << "Case #"<<k+1<<": Bad Magician!" << endl;
			
		}
		else if (count == 0)
		{
			ofile << "Case #"<<k+1<< ": Volunteer cheated! " << endl;
			
		}
	}
	file.close();
	ofile.close();
	return 0;
	
}
