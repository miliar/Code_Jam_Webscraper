#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <math.h>
using namespace std;

typedef unsigned long long ull;

ull binToKary(int n, int k)
{
	ull result = 0;
	int pw = 0;
	do
	{
		if (n % 2)
		{
			result += pow(k, pw);
		}
		n /= 2;
		pw++;
	}
	while (n > 0);
	return result;
}

ull divisor(ull n)
{
	ull rt = sqrt(n);
	for (ull i = 2; i <= rt; i++)
	{
		if (n % i == 0)
		{
			return i;
		}
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	ifstream infile("C.in");
	int T;
	if (!(infile >> T))
	{
		cerr << "Empty file!" << endl;
		return 1;
	}
	ofstream outfile("C.out");
	for (int i = 0; i < T; i++)
	{
		int N, J;
		infile >> N;
		infile >> J;
		cout << N << ' ' << J << endl;
		outfile << "Case #" << i + 1 << ": " << endl;
		int numFound = 0;
		int currNum = pow(2, N - 1) + 1;
		vector<ull> factors;
		/*vector<int> currNum;
		for (int j = 2; j <= 10; j++)
		{
			currNum.push_back(pow(j, N - 1) + 1);
		}*/
		while (numFound < J)
		{
			factors.clear();
			bool found = true;
			int factor = divisor(currNum);
			if (factor == 0)
			{
				found = false;
				factors.clear();
			}
			else
			{
				factors.push_back(factor);
			}
			ull baseKRep = currNum;
			for (int k = 3; k <= 10; k++)
			{
				baseKRep = binToKary(currNum, k);
				cout << baseKRep << endl;
				ull factor = divisor(baseKRep);
				if (factor == 0)
				{
					found = false;
					factors.clear();
					break;
				}
				else
				{
					factors.push_back(factor);
				}
			}
			if (found)
			{
				//outfile << currNum.back() << ' ';
				outfile << to_string(baseKRep) << ' ';
				for (int j = 2; j <= 10; j++)
				{
					outfile << factors[j - 2] << ' ';
				}
				outfile << endl;
				numFound++;
			}
			currNum += 2;
		}
	}
	return 0;
}