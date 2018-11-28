#include <iostream>
#include <string>
//#include <algorithm>
#include <vector>

using namespace std;

string solve(unsigned n)
{
	vector<unsigned> p;
    string ret;

	unsigned total = 0;
	for (unsigned i = 0 ; i < n; ++i)
	{
		unsigned pi = 0;
		cin >> pi;

	    p.push_back(pi);
		total += pi;
	}

	while (total > 0)
	{
		unsigned biggest_idx = n;
		unsigned biggest = 0;

		for (unsigned i = 0; i < n; ++i)
		{
			if (biggest_idx == n || biggest < p[i])
			{
				biggest_idx = i;
				biggest = p[i];
			}
		}

		if (total == 1)
		{
			cerr << "error!!" << endl;
			break;
		}

		unsigned second_idx = n;
		unsigned second = 0;
		for (unsigned i = 0; i < n; ++i)
		{
			if (i == biggest_idx)
				continue;

			if (second_idx == n || second < p[i])
			{
				second_idx = i;
				second = p[i];
			}
		}

		if (biggest - second >= 2)
		{
			ret += ' ';
			ret += (char)('A' + biggest_idx);
			ret += (char)('A' + biggest_idx);
			p[biggest_idx] -= 2;
			total -= 2;
		}
		else if (biggest - second == 1)
		{
			ret += ' ';
			ret += (char)('A' + biggest_idx);
			p[biggest_idx] -= 1;
			total -= 1;
		}
		else if (biggest == second)
		{
			if (total != 3)
			{
				ret += ' ';
				ret += (char)('A' + biggest_idx);
				ret += (char)('A' + second_idx);
				p[biggest_idx] -= 1;
				p[second_idx] -= 1;
				total -= 2;
			}
			else
			{
				ret += ' ';
				ret += (char)('A' + biggest_idx);
				p[biggest_idx] -= 1;
				total -= 1;
			}
		}
		else
		{
			cerr << "error!!!!" << endl;
		}
	}
	

	return ret;

}


int main()
{
	unsigned numInputs = 0;

	cin >> numInputs;

	for (size_t i=0; i< numInputs; ++i)
	{
		unsigned N = 0;
		cin >> N;

		cout << "Case #" << i + 1 << ":" << solve(N) << endl;
	}
	return 0;
}

