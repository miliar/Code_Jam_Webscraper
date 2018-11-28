#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int count = 0;
	int index = 0;
	int total = 0;
	int ansrow1 = 0;
	int ansrow2 = 0;
	bool flag = false;
	int arr1[4][4] = { 0 };
	int arr2[4][4] = { 0 };

	fstream f("A-small-attempt2.in", ios::in);
	fstream s("out.txt", ios::out);
	f >> total;
	
	for (int i = 0; i < total; i++)
	{
		f >> ansrow1;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				f >> arr1[j][k];
			}
		}
		f >> ansrow2;
		for (int l = 0; l < 4; l++)
		{
			for (int m = 0; m < 4; m++)
			{
				f >> arr2[l][m];
			}
		}
		
			for (int q = 0; q < 4; q++)
			{
				for (int w = 0; w < 4; w++)
				{

					if (arr1[ansrow1 - 1][q] == arr2[ansrow2 - 1][w])
					{
						flag = true;
						index = q;
						count++;
					}
				}
			}
			if (flag == true && count == 1)
			{
				s << "Case #" << i + 1 << ": " << arr1[ansrow1 - 1][index] << "\n";

			}
			else if (count > 1 && flag == true)
			{
				s << "Case #" << i + 1 << ": " << "Bad magician!\n";
			}
			else if (flag == false)
			{
				s << "Case #" << i + 1 << ": " << "Volunteer cheated!\n";
			}
		flag = false;
		count = 0;
	}

	f.close();
	s.close();


}