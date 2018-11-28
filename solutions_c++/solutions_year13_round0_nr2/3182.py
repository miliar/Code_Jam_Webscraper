#include <iostream>

bool test(int n, int m, int **f, int *m_rows, int *m_cols)
{
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if (f[i][j] < m_rows[i] && f[i][j] < m_cols[j])
			{
				return false;
			}
		}
	}
	return true;
}

int main()
{
	int t;
	std::cin >> t;
	for (int c = 0; c < t; ++c)
	{
		std::cout << "Case #" << c + 1 << ": ";
		int n, m;
		std::cin >> n >> m;
		int **f = new int *[n];

		int *m_rows = new int[n];
		int *m_cols = new int[m];
		for (int i = 0; i < n; m_rows[i++] = 0);
		for (int i = 0; i < m; m_cols[i++] = 0);

		for (int i = 0; i < n; ++i)
		{
			f[i] = new int[m];
			for (int j = 0; j < m; ++j)
			{
				std::cin >> f[i][j];
				if (f[i][j] > m_rows[i])
				{
					m_rows[i] = f[i][j];
				}
				if (f[i][j] > m_cols[j])
				{
					m_cols[j] = f[i][j];
				}
			}
		}
		std::cout << (test(n, m, f, m_rows, m_cols) ? "YES" : "NO") << std::endl;
	}
	return 0;
}
