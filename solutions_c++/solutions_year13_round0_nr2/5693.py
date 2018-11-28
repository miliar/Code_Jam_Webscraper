#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	int T, M, N;
	fstream in("B-small-attempt3.in", ios::in);
	fstream out("out.out", ios::out);

	in >> T;

	for (int k = 0; k < T; k++)
	{
		int min;
		int rMin = 0;
		int	cMin = 0;
		bool vert = 1;
		bool hor = 1;
		bool correct = 1;

		in >> N >> M;
		int **lawn = new int*[N];
		for (int i = 0; i < N; i++)
			lawn[i] = new int[M];

		int **allow = new int*[N];
		for (int i = 0; i < N; i++)
			allow[i] = new int[N];

		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
			{
				in >> lawn[i][j];
				allow[i][j] = 1;
			}
		min = 100;
		while (min != 101)
		{
		min = 101;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (lawn[i][j] == 1 && allow[i][j] == 1)
				{
					min = lawn[i][j];
					rMin = i;
					cMin = j;
				}

		allow[rMin][cMin] = 0;

		for (int j = 1; j < M; j++)
			if (lawn[rMin][j] != lawn[rMin][j-1])
				hor = false;

		for (int i = 1; i < N; i++)
			if (lawn[i][cMin] != lawn[i-1][cMin])
				vert = false;

			if (hor == false && vert == false)
			{
				correct = 0;
				break;
			}
			hor = true;
			vert = true;
		}
			if (correct)
				out << "Case #" << k+1 << ": YES" << endl;
			else
				out << "Case #" << k+1 << ": NO" << endl;

		for (int i = 0; i < N; i++)
			delete [] lawn[i];
		delete [] lawn;
	}
	in.close();
	out.close();

	system("pause");

	return 0;
}

