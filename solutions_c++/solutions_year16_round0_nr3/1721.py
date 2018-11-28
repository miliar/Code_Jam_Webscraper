#include <fstream>
#include <string>
#include <iostream>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

int128_t isprime(int128_t n)
{
	if (n % 2 == 0)
		return 2;

	int128_t md = boost::multiprecision::sqrt(n);

	int counter = 0;
	for (int i = 3; i <= md, counter < 100000; i += 2, counter++)
		if (n % i == 0)
			return i;

	return 0;
}

int128_t tobase(int b, string s)
{
	int p = s.length() - 1;

	int128_t r = 0;

	for (int i = 0; i < s.length(); i++, p--)
		if (s[i] == '1')
			r += boost::multiprecision::pow(int128_t(b), p);

	return r;
}

int main(int argc, char** argv)
{
	unsigned t = 1, n = 32, j = 500;

	ofstream output("output.out");

	vector<int128_t> data[500];

	for (int i = 1; i <= t; ++i)
	{
		int128_t f = boost::multiprecision::pow(int128_t(10), n - 1) + 1;

		int counter = 0;
		int q = 2;
		for (int128_t i = 10; i < f; i += boost::multiprecision::pow(int128_t(10), q), q++) {
			for (int128_t k = i; k < f; k *= 10)
			{
				vector<int128_t> line;

				int128_t m = f + k;

				line.push_back(m);

				auto sn = boost::lexical_cast<std::string>(m);

				cout << counter << endl;


				bool success = true;
				for (int b = 2; b < 10; b++)
				{
					auto h = tobase(b, sn);
					auto r = isprime(h);
					if (r != 0)
						line.push_back(r);
					else {
						success = false;
						break;
					}
				}

				if (!success)
					continue;

				int128_t r = isprime(m);

				if (r != 0)
					line.push_back(r);
				else
					continue;

				data[counter++] = line;

				if (counter == j)
					break;
			}

			if (counter == j)
				break;
		}

		q = 4;
		for (int128_t i = 1010; i < f; i += boost::multiprecision::pow(int128_t(10), q), q++) {
			for (int128_t k = i; k < f; k *= 10)
			{
				vector<int128_t> line;

				int128_t m = f + k;

				line.push_back(m);

				auto sn = boost::lexical_cast<std::string>(m);

				cout << counter << endl;


				bool success = true;
				for (int b = 2; b < 10; b++)
				{
					auto h = tobase(b, sn);
					auto r = isprime(h);
					if (r != 0)
						line.push_back(r);
					else {
						success = false;
						break;
					}
				}

				if (!success)
					continue;

				int128_t r = isprime(m);

				if (r != 0)
					line.push_back(r);
				else
					continue;

				data[counter++] = line;

				if (counter == j)
					break;
			}

			if (counter == j)
				break;
		}

		q = 5;
		for (int128_t i = 10010; i < f; i += boost::multiprecision::pow(int128_t(10), q), q++) {
			for (int128_t k = i; k < f; k *= 10)
			{
				vector<int128_t> line;

				int128_t m = f + k;

				line.push_back(m);

				auto sn = boost::lexical_cast<std::string>(m);

				cout << counter << endl;


				bool success = true;
				for (int b = 2; b < 10; b++)
				{
					auto h = tobase(b, sn);
					auto r = isprime(h);
					if (r != 0)
						line.push_back(r);
					else {
						success = false;
						break;
					}
				}

				if (!success)
					continue;

				int128_t r = isprime(m);

				if (r != 0)
					line.push_back(r);
				else
					continue;

				data[counter++] = line;

				if (counter == j)
					break;
			}

			if (counter == j)
				break;
		}

		output << "Case #" << i << ":" << endl;

		for (int i = 0; i < j; i++) {
			for (int k = 0; k < 10; k++)
				output << data[i].at(k) << ' ';

			output << endl;
		}
	}

	output.close();

	return 0;
}