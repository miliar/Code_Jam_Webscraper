#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

string magic(vector<vector<int>>, vector<vector<int>>, int, int);

int main()
{

	ifstream abre("A-small-attempt0.in");
	ofstream output("output.txt");
	int numCase;

	abre >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		int a, b;
		vector<vector<int>>mat1;
		vector<vector<int>>mat2;



		abre >> a;
	
		for (int j = 0; j < 4; j++)
		{
			vector<int>matTemp1;
			for (int k = 0; k < 4; k++)
			{
				int temp;
				abre >> temp;
				matTemp1.push_back(temp);
			}
			mat1.push_back(matTemp1);
		}

		abre >> b;

		for (int j = 0; j < 4; j++)
		{
			vector<int>matTemp2;
			for (int k = 0; k < 4; k++)
			{
				int temp;
				abre >> temp;
				matTemp2.push_back(temp);
				//cout << temp << " ";
			}
			mat2.push_back(matTemp2);
			//cout << endl;
		}
		
		output << "Case #" << (i + 1) << ": " << magic(mat1, mat2, a, b) << endl;

	}

	output.close();
	system("pause");
	return 0;
}

string magic(vector<vector<int>> m1, vector<vector<int>> m2, int a, int b)
{

	string resultado = "";
	int cont = 0;
	int res;

	/*for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cout << m1[i][j] << " ";
		}
		cout << endl;
	}

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cout << m2[i][j] << " ";
		}
		cout << endl;
	}*/

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (m1[a-1][i] == m2[b-1][j])
			{
				cont++;
				res = m1[a-1][i];
			}
		}
	}

	if (cont == 0)
	{
		resultado = "Volunteer cheated!";
	}

	if (cont == 1)
	{
		resultado = to_string(res);
	}

	if (cont >= 2)
	{
		resultado = "Bad magician!";
	}
	
	return resultado;
}