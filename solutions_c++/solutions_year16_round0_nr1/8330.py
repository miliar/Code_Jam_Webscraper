#include <iostream>
#include <fstream>
#include <vector>
#include <time.h>
#include <conio.h>

int main(int argc, char *argv[])
{
	clock_t Start = clock();
	std::ifstream In("In.txt");
	std::ofstream Out("Out.txt");

	unsigned int T;
	In >> T;

	for (unsigned int t = 0; t < T; t++)
	{
		unsigned long long n;
		In >> n;

		if (n == 0)
		{
			Out << "Case #" << t + 1 << ": INSOMNIA" << std::endl;
			continue;
		}

		unsigned int Found = 0;
		std::vector<bool> Digits;
		Digits.resize(10, false);

		unsigned long long Working = 0;
		while (Found != 10)
		{
			Working += n;

			unsigned long long Temp = Working;
			while (Temp > 0)
			{
				if (!Digits[Temp % 10])
				{
					Digits[Temp % 10] = true;
					Found++;
				}
				Temp /= 10;
			}
		}

		Out << "Case #" << t + 1 << ": " << Working << std::endl;

	}

	In.close();
	Out.close();

	clock_t End = clock();

	std::cout << (End - Start) * 1000 / CLOCKS_PER_SEC << "ms." << std::endl;
	_getch();
	return 0;
}