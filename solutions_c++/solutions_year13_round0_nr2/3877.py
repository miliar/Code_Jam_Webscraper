#include <iostream>
using namespace std;

int T, N, M;
int field[100][100], color[100][100];

bool check_row(int i, int max) {
    for (int j = 0; j < M; ++j)
		if (field[i][j] > max)
			return false;
	return true;
}

bool check_col(int j, int max) {
	for (int i = 0; i < N; ++i)
		if (field[i][j] > max)
			return false;
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	pair<int, int> tmp;
	bool OK;

	for (int I = 1; I <= T; ++I)
	{
		cin >> N >> M;
		
		OK = true;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				cin >> field[i][j];

		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
			{
				if (!check_row(i, field[i][j]) && !check_col(j, field[i][j]))
					OK = false;
			}
		
		if (OK)
			printf("Case #%d: YES\n", I);
		else
			printf("Case #%d: NO\n", I);
	}	

	return 0;
}

/*

*/