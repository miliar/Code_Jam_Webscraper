#include <stdio.h>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void ProcessNumber(unsigned long crt, unsigned long digits[], int& digitCount)
{
	while (crt != 0)
	{
		unsigned long d = crt % 10UL;
		if (digits[d] == 0)
		{
			digits[d] = 1;
			digitCount++;
		}
		crt = crt / 10UL;
	}
}

string Compute(unsigned long N)
{
	unsigned long digits[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	int digitCount = 0;

	unsigned long prev = N;

	unsigned long crt = N;

	unsigned long i = 1UL;
	while (true)
	{
		crt = i * N;
		unsigned long prev = (i - 1) * N;
		i++;

		ProcessNumber(crt, digits, digitCount);

		if (digitCount == 10)
			break;

		if (prev == crt || crt < prev)
		{
			return string("INSOMNIA");
		}
	}

	stringstream ss;
	ss << crt;

	return ss.str();
}

int main(int argc, char** argv)
{
	fstream fin;
	
	//fin.open("CountingSheep.in", std::ios::in);
	fin.open("A-large.in", std::ios::in);

	if (!fin.is_open())
		return -1;

	fstream fout;
	//fout.open("CountingSheep.out", std::ios::out);
	fout.open("A-large.out", std::ios::out);

	if (!fout.is_open())
		return -1;

	int T;
	
	fin >> T;

	for (int i = 0; i < T; i++)
	{
		unsigned long N;
		fin >> N;

		fout << "Case #" << (i + 1) << ": " << Compute(N).c_str() << std::endl;
	}

	
	fin.close();
	fout.close();

	return 0;
}