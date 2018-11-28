#include <assert.h>
#include <exception>
#include <iostream>
#include <fstream>
#include <string>
#include <boost/function.hpp>

using std::cout; using std::cin; using std::cerr; using std::endl;
using std::string;
using std::ios;

long long roundup(long long x)
{
    if (x < 0)
        return 0;

    --x;
    x |= x >> 1;
    x |= x >> 2;
    x |= x >> 4;
    x |= x >> 8;
    x |= x >> 16;
    x |= x >> 32;

    return x + 1;
}

long long rounddown(long long x)
{
	long long up = roundup(x);
	if (x == up)
		return x;
	return x / 2;
}

void precompute()
{
}

void test_case(std::istream &in, std::ostream &out, int case_num)
{
	int A, B, K;
	in >> A >> B >> K;

 	cout << "A=" << A << " B=" << B << " K=" << K << endl;
	long long opts = 0;
	for (int k = 0; k < K; k++)
		for (int a = 0; a < A; a++)
			for (int b = 0; b < B; b++)
			{
				if ((a & b) == k)
				{
					opts++;
				}
			}


	/*long long Azero[32], Bzero[32];
	long long Aones[32], Bones[32];

	for (int i = 0; i < 32; i++)
		Azero[i] = Bzero[i] = Aones[i] = Bones[i] = 0;

	for (int i = 0; i < 32; i++)
	{
		int n = 1 << i;
		if (A & n)
			for (int j = 0; j < i; j++)
			{
				Azero[j] += n / 2;
				Aones[j] += n / 2;
			}
		if (B & n)
			for (int j = 0; j < i; j++)
			{
				Bzero[j] += n / 2;
				Bones[j] += n / 2;
			}
	}

	for (int i = 0; i < 32; i++)
	{
		cout << "A0 " << Azero[i] << " A1 " << Aones[i] << endl;
	}

	long long opts = 0;
	for (long long k = 0; k < K; k++)
	{
		for (int i = 0; i < 32; i++)
		{
			int n = 1 << i;
			if (k & n)
				opts += Aones[i] * Bones[i];
			else
				opts += Aones[i] * Bzero[i] + Azero[i] * Bones[i] + Azero[i] * Bzero[i];
		}
	}*/

	out << "Case #" << case_num << ": " << opts << endl;
}

int main(int argc, const char *argv[])
{
	try
	{
		const string problem = "B";
		if (argc != 2)
		{
			cerr << "Usage: " << argv[0] << " ex|small-<n>|large-<n>" << endl;
			return 1;
		}

		const string in_filename = "source\\" + problem + "-" + argv[1] + ".in";
		std::ifstream in(in_filename.c_str(), ios::in);
		if (!in)
			throw std::runtime_error(in_filename + " not found");

		const string out_filename = "source\\" + problem + "-" + argv[1] + ".out";
		std::ofstream out(out_filename.c_str(), ios::out);
		if (!out)
			throw std::runtime_error(out_filename + " not found");

		precompute();

		int T;
		in >> T;
		for (int t = 1; t <= T; t++)
		{
			test_case(in, out, t);
		}

		out.close();
		in.close();

		return 0;
	}
	catch (std::exception &e)
	{
		cerr << "ERROR: " << e.what() << endl;
	}
	catch (...)
	{
		cerr << "UNKNOWN ERROR (...)" << endl;
	}

	return 1;
}

