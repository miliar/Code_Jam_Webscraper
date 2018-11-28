#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

bool isPrime(long long n, int& non_trivial_divisor)
{
	for (int i = 2; i <= (int)sqrt(n); ++i)
	{
		if (n%i == 0)
		{
			non_trivial_divisor = i;
			return false;
		}
	}

	return true;
}

vector<string> jamcoin_helper(int length)
{
	vector<string> jamcoins;

	if (length == 1)
	{
		jamcoins.push_back("0");
		jamcoins.push_back("1");
		return jamcoins;
	}
	
	vector<string> jamcoins_remainder = jamcoin_helper(length - 1);
	for (int i = 0; i < jamcoins_remainder.size(); ++i)
	{
		jamcoins.push_back("0" + jamcoins_remainder[i]);
		jamcoins.push_back("1" + jamcoins_remainder[i]);
	}

	return jamcoins;
}

long long get_value_by_base(string jamcoin, int base)
{
	long long value = 0;

	for (int i = jamcoin.size() - 1; i >= 0; --i)
	{
		if (jamcoin.at(i) == '1')
			value += pow(base, jamcoin.size() - i - 1);
	}

	return value;
}

vector<string> get_jamcoin(int length, int n)
{
	vector<string> jamcoins;

	vector<string> temp;
	vector<string> jamcoinHelper = jamcoin_helper(length - 2);
	for (int i = 0; i < jamcoinHelper.size(); ++i)
	{
		temp.push_back("1" + jamcoinHelper[i] + "1");
	}

	int count = 0;
	stringstream ss;
	int divisor;

	for (int i = 0; i < temp.size(); ++i)
	{
		ss.str(string());
		ss.clear();
		ss << temp[i] + " ";

		int j;
		for (j = 2; j <= 10; ++j)
		{
			long long v = get_value_by_base(temp[i], j);
			if (isPrime(v, divisor))
				break;
			
			ss << divisor << " ";
		}

		if (j == 11)
		{
			ss << endl;
			jamcoins.push_back(ss.str());
			
			++count;
		}

		if (count >= n)
			break;
	}

	return jamcoins;
	
}

int main()
{
	ifstream in_file("C-small-attempt1.in");
	ofstream out_file("output.txt");

	if (in_file.is_open() && out_file.is_open())
	{
		string line;
		int i = 1, temp;
		getline(in_file, line);

		while (getline(in_file, line))
		{
			if (line == "")
				break;

			int N = stoi(line.substr(0, line.find(" ")));
			int J = stoi(line.substr(line.find(" "), line.size()));
			vector<string> output = get_jamcoin(N, J);

			out_file << "Case #" << i << ":" << endl;
			for (int j = 0; j < output.size(); ++j)
			{
				out_file << output[j];
			}

			++i;
		}
	}

	in_file.close();
	out_file.close();

	return 0;
}