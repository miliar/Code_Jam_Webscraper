#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>

std::ifstream in("input.in");
std::ofstream out("output.txt");

char mine = '*';

typedef std::vector<char> tRow;
typedef std::vector<tRow> tMatrix;

void printMatrix(tMatrix& m, int r, int c)
{
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (m[i][j] == mine)
				out << '*';
			else if (i == 0 && j == 0)
				out << 'c';
			else 
					out << '.';
		}
		out << std::endl;
	}
}

struct data
{
	long long A;
	long long B;
	long long K;
};

void printM(const tMatrix& m, int r, int c)
{
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			std::cout << (int)m[i][j] << " ";
		}
		std::cout << std::endl;
	}
}

void test(data& d)
{
	long long A = d.A;
	long long B = d.B;
	long long K = d.K;
	//std::cout << "A = " << A << ", B = " << B << ", K = " << K << std::endl;
	long long max = std::max(A, B);
	long long min = std::min(A, B);
	long long m = std::min(min, K);
	long long count = 0;
	for (long long i = 0; i < min; ++i)
	{
		for (long long j = 0; j < max; ++j)
		{
			if ((i&j) < K)
				++count;
		}
	}
	out << count << std::endl;
}

int main()
{
	int numOfTCs;
	in >> numOfTCs;
	std::vector<data> tests(numOfTCs);
	for (int i = 0; i < numOfTCs; ++i)
	{
		in >> tests[i].A >> tests[i].B >> tests[i].K;
	}

	for (int i = 1; i <= numOfTCs; ++i)
	{
		out << "Case #" << i << ": ";
		test(tests[i-1]);
	}
}
