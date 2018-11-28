#include"iostream"
#include"unordered_set"
using namespace std;
int main()
{
	int Times = 0;
	::cin >> Times;

	for (int seek = 0; seek<Times; seek = seek + 1)
	{
		int N = 0;
		::cin >> N;

		::cout << "Case #" << seek + 1 << ": ";

		if (N == 0){ ::cout << "INSOMNIA" << endl; continue; }

		int DigitsCount = 10;
		bool DigitsArray[10] = { false, false, false, false, false, false, false, false, false, false };

		int CurrentTime = 1;
		while (DigitsCount != 0)
		{
			unsigned long long CurrentNum = N * CurrentTime;

			while (CurrentNum != 0)
			{
				int Digit = CurrentNum % 10;
				CurrentNum = CurrentNum / 10;

				DigitsCount = DigitsCount - (DigitsArray[Digit] ? 0 : 1);

				DigitsArray[Digit] = true;
			}

			if (DigitsCount <= 0){ break; }
			CurrentTime = CurrentTime + 1;
		}

		::cout << N * CurrentTime << endl;
	}

	return 0;
}