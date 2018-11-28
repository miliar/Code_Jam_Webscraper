#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int numberOfTests;
	in >> numberOfTests;
	for (int t = 1; t <= numberOfTests; t++)
	{
		int N;
		in >> N;

		

		int arrOfDigits[10];

		for (int i = 0; i < 10; i++)
			arrOfDigits[i] = 0;		

		int i = 0;

		bool haveZero;
		if (N == 0) haveZero = false;
		else haveZero = true;
		while(haveZero)
		{
			int addVar = N * ++i;
			while (addVar != 0)
			{
				arrOfDigits[addVar % 10]++;
				addVar /= 10;
			}
			haveZero = false;
			for (int j = 0; j < 10;j++)
				if (arrOfDigits[j] == 0)
				{
					haveZero = true;
					break;
				}			
		}
		out << "Case #" << t << ": ";
		if (N != 0) out << N * i << endl;
		else out << "INSOMNIA" << endl;
	}

	return 0;
}
