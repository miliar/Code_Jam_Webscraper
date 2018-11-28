#include <iostream>

void solvecase(int lawn[100][100], int N, int M, int idx)
{
	for (int i = 0; i < N; i++)
	{
		bool equal = true;

		for (int j = 0; j < M; j++)
		{
			if (lawn[i][j] != lawn[i][0])
			{
				equal = false;
				break;
			}
		}

		if (!equal)
		{
			int max = lawn[i][0];
			
			for (int j = 0; j < M; j++)
			{
				if (lawn[i][j] > max)
				{
					max = lawn[i][j];
				}
			}

			for (int j = 0; j < M; j++)
			{
				if (lawn[i][j] != max)
				{
					for (int c = 0; c < N; c++)
					{
						if (lawn[c][j] > lawn[i][j])
						{
							std::cout<<"Case #" << idx << ": NO" << std::endl;
							return;
						}
					}
				}
			}


		}

	}

	std::cout<<"Case #" << idx << ": YES" << std::endl;

}


int main(int argc, char* argv[])
{
	int n = 0;
	std::cin >> n;

	int lawn[100][100];

	for (int i = 0; i < n; i++)
	{
		int N,M;

		std::cin >> N;
		std::cin >> M;

		for (int r = 0; r < N; r++)
		{
			for (int c = 0; c < M; c++)
				std::cin >> lawn[r][c];
		}
		
		solvecase(lawn, N , M, i+1);
	}


	return 0;
}
