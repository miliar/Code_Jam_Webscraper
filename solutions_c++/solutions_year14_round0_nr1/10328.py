#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	const int grid = 4;
	ifstream in("Qualification_1.in");
	ofstream out("Qualification_1.out");
	int tests, ans_1, ans_2, arr_1[grid][grid], arr_2[grid][grid], storage_1[grid], storage_2[grid], counter = 0, sol = 0;
	bool flag = false, flag2 = false;
	in >> tests;
	//cout << tests << endl;
	for (int i = 0; i < tests; i++)
	{
		counter = 0;
		in >> ans_1;
		//cout <<ans_1 << endl;
		for (int j = 0; j < grid; j++)
		{
			for (int k = 0; k < grid; k++)
			{
				in >> arr_1[j][k];
				//cout << arr_1[j][k] << " ";
			}//end for grid_k
			//cout << endl;
		}//end for grid_j
		in >> ans_2;
		//cout << ans_2 << endl;
		for (int l = 0; l < grid; l++)
		{
			for (int m = 0; m < grid; m++)
			{
				in >> arr_2[l][m];
				//cout << arr_2[l][m]<<" ";
			}//end for grid_m
			//cout << endl;
		}//end for grid_l
		/*cout << endl;*/
		for (int a = ans_1 - 1; a < ans_1; a++)
		{
			for (int b = 0; b < grid; b++)
			{
				storage_1[b] = arr_1[a][b];
				//cout << storage_1[b] << " ";
			}//end for b
			//cout << endl;
		}//end for a
		for (int c = ans_2 - 1; c < ans_2; c++)
		{
			for (int d = 0; d < grid; d++)
			{
				storage_2[d] = arr_2[c][d];
				//cout << storage_2[d] << " ";
			}//end for b
			//cout << endl;
		}//end for a
		for (int e = 0; e < 4; e++)
		{
			for (int f = 0; f < 4; f++)
			{
				//cout << storage_1[e] << " compared with " << storage_2[f] << endl;
				if (storage_1[e] == storage_2[f])
				{
					counter++;
					//cout << storage_1[e] << endl;
					sol = storage_1[e];
					//break;
				}//end if
				//else if (counter>1)
				//{
				//	cout << "Bad magician\n";
				//	flag = true;
				//}//end else-if
				//else if (counter < 1)
				//{
				//	cout << "Volunteer cheated\n";
				//	flag = true;
				//}//ens else-if_2
			}//end for f
			if (flag)
			{
				//break;
			}//end if
		}//end for e
		if (counter > 1)
		{
			cout<< "Case #"<< i+1<<": " << "Bad magician!\n";
			out << "Case #" << i + 1 << ": " << "Bad magician!\n";
			//break;
		}//end elif
		else if (counter < 1)
		{
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!\n";
			out << "Case #" << i + 1 << ": " << "Volunteer cheated!\n";
			//break;
		}//end elif-2
		else if (counter == 1)
		{
			cout << "Case #" << i + 1 << ": " << sol << endl;
			out << "Case #" << i + 1 << ": " << sol << endl;
			//break;
		}//end if
		//system("pause");//for one case
	}//end for tests_i
	return 0;
}//end main