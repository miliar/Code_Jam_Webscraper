#include <fstream>
using namespace std;

int main()
{
	unsigned int		T, nIndex = 0, N;

	ifstream	InFile("A-large.in");
	ofstream	OutFile("A-large.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open() && InFile.is_open())
	{
		InFile >> T;

		while (T--)
		{
			InFile >> N;

			if (N == 0)
			{
				OutFile << "Case #" << ++nIndex << ": INSOMNIA" << endl;
				continue;
			}

			bool	DigitsSeen[10] = {0};

			for (int i = 0; i < INT_MAX; i += N)
			{
				unsigned int N_OP = N + i;

				while (N_OP)
				{
					DigitsSeen[N_OP % 10] = true;
					N_OP /= 10;
				}

				bool	bAllDigitsSeen = true;

				for (int ii = 0; ii < 10; ++ii)
				{
					if (DigitsSeen[ii] == false)
					{
						bAllDigitsSeen = false;
						break;
					}
				}

				if (bAllDigitsSeen)
				{
					OutFile << "Case #" << ++nIndex << ": " << (N + i) << endl;
					break;
				}
			}
		}
	}

	return 0;
}