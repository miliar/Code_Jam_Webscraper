#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool fallSleep(bool found[]);
void digitFound(bool found[], int dig);
void resetArray(bool found[]);

int main()
{
	long long N, temp;
	int T, digit, n, count;
	string file;
	bool found[10] = { false, false, false, false, false, false, false, false, false, false};

	ifstream input;
	ofstream output;

	cout << "Filename : ";
	getline(cin, file);

	input.open(file + ".in");
	output.open(file + ".out");

	input >> T;

	for (int i = 0; i < T; i++)
	{
		resetArray(found);
		input >> N;
		n = 1;
		count = 0;
		
		while (true)
		{
			temp = N * n;

			while (temp != 0)
			{
				digit = temp % 10;

				digitFound(found, digit);

				temp /= 10;
			}

			if (N == 0 || count >= 100)
			{
				output << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
				break;
			}

			else if (fallSleep(found))
			{
				output << "Case #" << i + 1 << ": " << N * n << endl;
				break;
			}

			n++;
			count++;
		}

	}

	return 0;
}

bool fallSleep(bool found[])
{
	for (int i = 0; i < 10; i++)
		if (found[i] == false)
			return false;

	return true;
}

void digitFound(bool found[], int dig)
{
	found[dig] = true;
}

void resetArray(bool found[])
{
	for (int i = 0; i < 10; i++)
		found[i] = false;
}