#include <iostream>
#include <vector>

using namespace std;
#pragma warning(disable:4996)

typedef unsigned int uint;

bool checkDigit(uint digit, uint value)
{
	while (value > 0)
	{
		if (value % 10 == digit)
			return true;

		value /= 10;
	}

	return false;
}

int main()
{
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Dilum\\Desktop\\SingaJob\\GoogleCodeJam_2016\\Debug\\output.txt", "w", stdout);

	uint N;
	uint status;

	uint testCases;
	cin >> testCases;
	uint caseNumber = 1;
	while (caseNumber <= testCases)
	{
		uint count = 2;
		status = 0x0000;

		cin >> N;
		uint value = N;

		if (N != 0)
		{
			while (status != 0x3FF)
			{
				if (!(status & 0x1)) // check for one
				{
					if (checkDigit(1, value))
						status |= 0x1;
				}

				if (!(status & 0x2)) // check for two
				{
					if (checkDigit(2, value))
						status |= 0x2;
				}

				if (!(status & 0x4)) // check for three
				{
					if (checkDigit(3, value))
						status |= 0x4;
				}

				if (!(status & 0x8)) // check for four
				{
					if (checkDigit(4, value))
						status |= 0x8;
				}

				if (!(status & 0x10))
				{
					if (checkDigit(5, value))
						status |= 0x10;
				}

				if (!(status & 0x20))
				{
					if (checkDigit(6, value))
						status |= 0x20;
				}

				if (!(status & 0x40))
				{
					if (checkDigit(7, value))
						status |= 0x40;
				}

				if (!(status & 0x80))
				{
					if (checkDigit(8, value))
						status |= 0x80;
				}

				if (!(status & 0x100))
				{
					if (checkDigit(9, value))
						status |= 0x100;
				}

				if (!(status & 0x200))
				{
					if (checkDigit(0, value))
						status |= 0x200;
				}

				if (status == 0x3FF)
				{
					cout << "Case #" << caseNumber << ": " << value << endl;
					break;
				}

				value = N * count;
				++count;
			}
		}
		else
		{
			cout << "Case #" << caseNumber << ": INSOMNIA" << endl;
		}

		++caseNumber;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
