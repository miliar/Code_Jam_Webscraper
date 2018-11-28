#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <limits>
using namespace std;

// #pragma warning(disable: 4018)
// #include "../my_header.h"


struct solver
{
	bool are_eq(const char *str1, const char *str2, int n)
	{
		for (int i=0 ; i < n ; i++)
			if (str1[i] != str2[i])
				return false;
		return true;
	}

	int search(int K, int L, int S, const char *word, const char *keys, char *buff, int idx, long long &counter, int &max_hits)
	{
		if (idx == S)
		{
			int local_count = 0;
			for (int i=0 ; i <= S - L ; i++)
				if (are_eq(word, buff+i, L))
					local_count++;
			counter += local_count;
			if (local_count > max_hits)
				max_hits = local_count;
		}
		else
		{
			for (int i=0 ; i < K ; i++)
			{
				buff[idx] = keys[i];
				search(K, L, S, word, keys, buff, idx+1, counter, max_hits);
			}
		}
	}

	double brute_force_solve(int K, int L, int S, const char *word, const char *keys)
	{
		char *buff = new char[S];
		long long counter = 0;
		int max_hits = 0;

		search(K, L, S, word, keys, buff, 0, counter, max_hits);

		long long combinations = 1;
		for (int i=0 ; i < S ; i++)
			combinations *= K;

		double exp_hits = double(counter) / double(combinations);

		return max_hits - exp_hits;
	}

	double solve(int K, int L, int S, const char *word, const char *keys)
	{
		return brute_force_solve(K, L, S, word, keys);
	}
};

/*************************************************************************************/

void process_test_case(int case_num, ifstream &ifs, ofstream &ofs)
{
	int K, L, S;
	ifs >> K >> L >> S;

	string keys, word;
	ifs >> keys >> word;

	cerr << K << " " << L << " " << S << " " << keys << " " << word << endl;

	double res = solver().solve(K, L, S, word.c_str(), keys.c_str());

	cout << "Case #" << case_num << ": " << res << endl;
	ofs << "Case #" << case_num << ": " << res << endl;
}

/*************************************************************************************/

int main(int argc, char **argv)
{
	if (argc != 3) {
		cout << "Usage: runme <input file> <output file>" << endl;
		return 1;
	}

	ifstream ifs(argv[1], ifstream::in);
	ofstream ofs(argv[2]);

	ofs.precision(8);
	ofs << fixed;

	int T;
	ifs >> T;
	// assert(T > 0 && T < 200);

	for (int i=0 ; i < T ; i++)
	{
		// if (i > 0)
		// 	cout << "\n---------------------------------------------\n\n";
		process_test_case(i+1, ifs, ofs);
	}

	return 0;
}
