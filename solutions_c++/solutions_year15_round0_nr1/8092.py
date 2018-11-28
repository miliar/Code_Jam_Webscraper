#include <iostream>
#include <fstream>
#define MAX 1001

int P[MAX];
int SO[MAX];
int req;
int i, temp;

void reset()
{
	req = 0;
	i = 0;
}
void next(int pip1)
{
	P[i] = pip1;

	if (i == 0)
	{
		SO[0] = 0;
	}
	else
	{
		temp = SO[i - 1] + P[i - 1];
		if (temp >= i)
		{
			SO[i] = temp;
		}
		else
		{
			SO[i] = P[i - 1] + i;
			req += (i - SO[i - 1]);
		}
	}

	++i;
}

int main()
{
	std::ifstream inputFile("input", std::ios::in);
	std::ofstream outputFile("output", std::ios::out);

	int cases = 0, sMax = 0, num;
	inputFile >> cases;
	char ch;

	for (int c = 1; c <= cases; ++c)
	{
		reset();
		inputFile >> sMax;

		for (int ci = 0; ci <= sMax; ++ci)
		{
			inputFile >> ch;
			num = atoi(&ch);
			next(num);
		}

		outputFile << "Case #" << c << ": " << req << std::endl;
	}

	inputFile.close(); outputFile.close();
	system("PAUSE");
	return 0;
}