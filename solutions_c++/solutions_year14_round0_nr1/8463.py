#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream fin("A.in", ios::in);
	ofstream fout("A.out", ios::out);

	int T;

	fin >> T;

	for (int i = 0; i < T; i++)
	{
		vector<int> uno, dos;

		for (int j = 0; j < 2; j++)
		{
			int fila;
			fin >> fila;

			int n1, n2, n3, n4;
			for (int k = 0; k < 4; k++)
			{
				fin >> n1 >> n2 >> n3 >> n4;

				if (j == 0 && fila == k + 1)
				{
					uno.push_back(n1);
					uno.push_back(n2);
					uno.push_back(n3);
					uno.push_back(n4);
				}

				if (j == 1 && fila == k + 1)
				{
					dos.push_back(n1);
					dos.push_back(n2);
					dos.push_back(n3);
					dos.push_back(n4);
				}
			}
		}


		int mag = 0, card = 0;
		for (int m = 0; m < 4; m++)
		{
			for (int i = 0; i < 4; i++)
			{
				if (uno[m] == dos[i])
				{
					mag++;
					card = uno[m];
				}
			}
		}

		if (mag == 0)
			fout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		else if (mag == 1)
			fout << "Case #" << i + 1 << ": " << card << endl;
		else if (mag > 1)
			fout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
	}


	fout.close();

	return 0;
}