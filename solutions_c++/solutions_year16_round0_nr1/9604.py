#include <iostream>
using namespace std;

int main()
{
	int N, T, x, broj,winningBroj,z;
	char digits[10] = {0};
	bool isAsleep = false;
	
	std::cin >> T;

	for (int i = 0; i < T; i++)
	{
		std::cin >> N;
		isAsleep = false;
		x = 0;
		if (N != 0)
		{
			while (!isAsleep)
			{
				x += N;
				broj = x;
				while (broj > 0)
				{
					digits[broj % 10] = 1;
					broj /= 10;
				}
				broj = x;
				isAsleep = true;
				for (z = 0; z < 10; z++)
				{
					if (digits[z] == 0)
					{
						isAsleep = false;
						break;
					}
				}
			}
			if (isAsleep)
			{
				cout << "Case #" << i + 1 << ": " << broj << endl;
			}
		}
		else
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		fill(digits, digits + 10, 0);
	}

	return 0;
}