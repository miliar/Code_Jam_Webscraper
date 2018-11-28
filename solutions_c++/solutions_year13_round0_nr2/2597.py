#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int a[100][100];
int maxh[100], maxv[100];

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
		int h, w;
		std::cin >> h >> w;
		bool ok = true;

		for (int i = 0 ; i < h ; ++i)
			maxh[i] = 0;
		for (int j = 0 ; j < w ; ++j)
			maxv[j] = 0;
		for (int i = 0 ; i < h ; ++i)
		{
			for (int j = 0 ; j < w ; ++j)
			{
				std::cin >> a[i][j];
				maxh[i] = std::max(maxh[i], a[i][j]);
				maxv[j] = std::max(maxv[j], a[i][j]);
			}
		}

		for (int i = 0 ; i < h ; ++i)
		{
			for (int j = 0 ; j < w ; ++j)
			{
				if (a[i][j] != maxh[i] && a[i][j] != maxv[j])
					ok = false;
			}
		}
			/*
		for (int k = 0 ; ok && k < w + h ; ++k)
		{
			bool found = false;
			for (int i = 0 ; !found && i < w ; ++i)
			{
				if (!bv[i])
				{
					int c = a[0][i];
					for (int j = 1 ; c >= 0 && j < h ; ++j)
						if (c == 0)
							c = a[j][i];
						else if (a[j][i] && c != a[j][i])
							c = -1;
					std::cout << "- V: " << i << " " << c << "\n";
					if (c >= 0)
					{
						found = true;
						bv[i] = true;
						for (int j = 0 ; j < h ; ++j)
							a[j][i] = 0;
					}
				}
			}
			if (!found)
			{
				for (int i = 0 ; !found && i < h ; ++i)
				{
					if (!bh[i])
					{
						int c = a[i][0];
						for (int j = 1 ; c >= 0 && j < w ; ++j)
							if (c == 0)
								c = a[i][j];
							else if (a[i][j] && c != a[i][j])
								c = -1;
						std::cout << "- H: " << i << " " << c << "\n";
						if (c >= 0)
						{
							found = true;
							bh[i] = true;
							for (int j = 0 ; j < w ; ++j)
								a[i][j] = 0;
						}
					}
				}
			}
			if (!found)
				ok = false;
		}
		*/

		std::cout << "Case #" << t << ": " << (ok ? "YES" : "NO") << "\n";
	}
	return 0;
}

