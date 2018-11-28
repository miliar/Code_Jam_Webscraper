#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("C.txt");
	ofstream out("C_ans.txt");

	
	int testnum;
	in >> testnum;
	for (int t = 0; t < testnum; t++)
	{
		char a[100][100];
		int R, C, M;
		in >> R >> C >> M;
		int R1 = R, C1 = C;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				a[i][j] = '.';


		if (C == 1)
		{
			for (int i = R-M+1; i <= R; i++)
				a[i][1] = '*';
			M = 0;
		}
		else
		if (R == 1)
		{
			for (int j = C-M+1; j <= C; j++)
				a[1][j] = '*';
			M = 0;
		}
		else
		while (M > 0)
		{
			if (C1 == R1 && C1 == 3 && M == C1-1)
				break;

			if ((C1 == 1 && M < R1-1) || (R1 == 1 && M < C1-1))
			{
				M = 10;
				break;
			}

			if (C1 > R1)
			{
				if (M >= (C1-R1)*R1)
				{
					for (int i = 1; i <= R1; i++)
						for (int j = R1+1; j <= C1; j++)
							a[i][j] = '*';
					M -= R1*(C1-R1);
					C1 = R1;
				}
				else
				{
					while (M >= R1)
					{
						for (int i = 1; i <= R1; i++)
							a[i][C1] = '*';
						M -= R1;
						C1--;
					}

					if (R1 == 2 && M > 0)
						break;

					int t = R1;
					while (M > 0 && t > 2)
					{
						a[t][C1] = '*';
						M--;
						t--;
					}
					t = C1-1;
					while (M > 0)
					{
						a[R1][t] = '*';
						M--;
						t--;
					}

				}
			}
			else
			if (C1 < R1)
			{
				if (M >= (R1-C1)*C1)
				{
					for (int j = 1; j <= C1; j++)
						for (int i = C1+1; i <= R1; i++)
							a[i][j] = '*';
					M -= C1*(R1-C1);
					R1 = C1;
				}
				else
				{
					while (M >= C1)
					{
						for (int j = 1; j <= C1; j++)
							a[R1][j] = '*';
						M -= C1;
						R1--;
					}

					if (C1 == 2 && M > 0)
						break;


					int t = C1;
					while (M > 0 && t > 2)
					{
						a[R1][t] = '*';
						M--;
						t--;
					}
					t = R1-1;
					while (M > 0)
					{
						a[t][C1] = '*';
						M--;
						t--;
					}
				}
			}
			else
			{
				if (M >= R1)
				{
					for (int i = 1; i <= R1; i++)
						a[i][C1] = '*';
					C1--;
					M -= R1;
				}
				else
				{
					if (C1 == 2)
						break;

					int t = R1;
					while (M > 0 && t > 2)
					{
						a[t][C1] = '*';
						M--;
						t--;
					}
					t = C1-1;
					while (M > 0)
					{
						a[R1][t] = '*';
						M--;
						t--;
					}
				}
			}


			if ((C1 == 1 && M < R1-1) || (R1 == 1 && M < C1-1))
			{
				M = 10;
				break;
			}
		}

		a[1][1] = 'c';

		out << "Case #" << t+1 << ":" << endl;
		if (M > 0)
			out << "Impossible" << endl;
		else
		{
			for (int i = 1; i <= R; i++)
			{
				for (int j = 1; j <= C; j++)
					out << a[i][j];
				out << endl;
			}
		}
	}
	return 0;
}


