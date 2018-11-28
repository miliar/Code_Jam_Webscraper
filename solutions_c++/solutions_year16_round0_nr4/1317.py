//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/multiprecision/gmp.hpp>
#include <boost/multiprecision/cpp_int.hpp>
//#include <boost/multiprecision/mpfr.hpp>

#include <string>
#include <bitset>
#include <vector>

#include <cstdlib>
#include <cstring>

using namespace std;
using namespace boost;
using namespace multiprecision;

typedef number<gmp_float<10000> > mpf_float_10000;

mpz_int get_tile_combination(vector<int> seq, int K, int C)
{
	mpz_int tile = 0;

	for (unsigned c = 0; c < seq.size(); c++)
	{
		//cout << "C - c - 1 " << C - c - 1 << endl;
		//cout << "seq[c] " << seq[c] << endl;

		mpf_float_1000 tile_float = ((seq[c]) * pow(mpf_float_1000(K), mpf_float_1000(C-c-1)));

		if (tile_float < 0)
		{
			cout << "OUCH " << tile_float << endl;
		}

		tile += tile_float.convert_to<mpz_int>();
	}

	// indexing from 1
	tile += 1;

	return tile;
}


int main() {


	//vector<int> seq;
	//seq.push_back(1);
	//cout << get_tile_combination(seq, 2, 1);

	int T;

	cin >> T;

	BOOST_FOREACH(int t, irange(0, T))
	{
		int K, C, S;

		cin >> K;
		cin >> C;
		cin >> S;

		mpz_int tile = 0;

		cout << "Case #" << (t+1) << ":";

		if (C >= K)
		{
			// only need to check 1 tile
			// 1-2-3-etc

			vector<int> seq;

			for (int k = 0; k < K; k++)
			{
				seq.push_back(k);
			}

			tile = get_tile_combination(seq, K, C);

			cout << " " << tile;
		}
		else
		{
			// need to check ceil(K/C) tiles

			int num_tiles = ceil((double)K/(double)C);

			if (num_tiles > S)
			{
				cout << " IMPOSSIBLE";
			}


			int current_comb = 0;
			int k_remaining = K;

			for (int n = 0; n < num_tiles; n++)
			{


				vector<int> seq;


				int chunk = min(C, k_remaining);
				for (int c = 0; c < chunk; c++)
				{
					seq.push_back(current_comb);
					current_comb++;
					k_remaining--;
				}

				tile = get_tile_combination(seq, K, C);

				cout << " " << tile;

			}

		}

		cout << "\n";
	}

	cout.flush();


	return 0;
}
