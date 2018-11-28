#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T;

	fin >> T;

	for (int i = 0; i < T; ++i)
	{
		int N, M;
		fin >> N >> M;

		vector<vector<unsigned short>> field;
		vector<unsigned short> emptyVector;

		/*char minValue = 100;*/

		for (int n = 0; n < N; ++n)
		{
			field.push_back(emptyVector);
			for (int m = 0; m < M; ++m)
			{
				unsigned short tmp;
				fin >> tmp;
				field[n].push_back(tmp);
				/*if (tmp < minValue)
					minValue = tmp;*/
			}
		}
		
		bool result = true;

		for (int n = 0; n < N; ++n)
		{
			for (int m = 0; m < M; ++m)
			{
				//OLD VAR
				bool hor = true;
				bool ver = true;
				//hor
				for (int w = 0; w < M; ++w)
				{
					if (field[n][w] > field[n][m])
					{
						hor = false;
						break;
					}
				}
				//ver
				for (int h = 0; h < N; ++h)
				{
					if (field[h][m] > field[n][m])
					{
						ver = false;
						break;
					}
				}
				result = hor | ver;
				if (!result)
					break;

				//cout << "Done: " << long double((i  + 1) * (n + 1) * (m + 1)) / 1000000 * 100 << "%" << "curT = " << i + 1 << endl;
				//OLDVAR


				/*result = (field[n][m] == field[0][m]) | (field[n][m] == field[n][0]);
				if (!result)
					break;*/
			}
			if (!result)
				break;
		}

		if (result)
			fout << "Case #" << i + 1 << ": YES" << endl;
		else
			fout << "Case #" << i + 1 << ": NO" << endl;
	}

	fin.close();
	fout.close();

	return 0;
}