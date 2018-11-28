#include <iostream>

int main(int argc, char ** argv)
{
	int num;
	std::cin >> num;

	for (int c = 0; c < num; c++)
	{
		int n, m;
		std::cin >> n >> m;

		int * lawn = new int[n * m];
		for (int i = 0; i < n * m; i++)
			std::cin >> lawn[i];

		int * max = new int[n+m];
		for (int i = 0; i < n + m; i++)
			max[i] = 0;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				int l = lawn[i*m+j];
				max[i]   = std::max(max[i],   l);
				max[n+j] = std::max(max[n+j], l);
			}

		bool yes = true;
		for (int i = 0; i < n && yes; i++)
			for (int j = 0; j < m && yes; j++)
			{
				int l = lawn[i*m+j];
				if (l < max[i] && l < max[n+j])
					yes = false;
			}

		std::cout << "Case #" << c + 1 << ": " << (yes ? "YES" : "NO") << std::endl;
	}

	return 0;
}