#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>

using namespace std;

int used;
const int check = 1023;

bool findDigits(long long num)
{
	do {
		int digit = num % 10;

		used |= (1 << digit);

		if (used == check)
			return true;

		num /= 10;
	} while (num > 0);

	return false;
}

int main()
{
	fstream in("in.in"), out("out.txt");

	srand(time(NULL));

	int T;

	in >> T;

	for (int t = 1; t <= T; ++t)
	{
		int n, i = 1;
		used = 0;

		long long num;

		in >> n;

		while (true)
		{
			num = i * n;

			if (n == 0)
			{
				out << "Case #" << t << ": " << "INSOMNIA" << endl;
				break;
			}

			if (findDigits(num))
			{
				out << "Case #" << t << ": " << num << endl;
				break;
			}

			++i;
		}
	}

	in.close();
	out.close();

	return 0;
}