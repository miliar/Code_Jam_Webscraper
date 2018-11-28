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
#include <string>
#include <bitset>
#include <vector>
#include <sstream>

#include <cstdlib>
#include <cstring>

#include <boost/multiprecision/gmp.hpp>

using namespace std;
using namespace boost;
using namespace multiprecision;




int main() {

	int T;

	cin >> T;

	BOOST_FOREACH(int t, irange(0, T))
	{
		int N, J;

		cin >> N;
		cin >> J;

		cout << "Case #" << (t+1) << ":\n";



		int bits_to_change = N - 2;
		unsigned max_number = (1 << (bits_to_change));

		/*bitset<32> max_num(max_number);
		for (int j = N-1; j >=0; j--)
		{
			cout << max_num.test(j) ? '1' : '0';
		}

		exit(0);*/

		int jam_coin_head_and_tail = 1 + (1 << (N - 1));


		string sep = "";
		for (unsigned i = 0; i < max_number; i++)
		{
			bitset<32> num((i<<1)+jam_coin_head_and_tail);



			ostringstream os;

			for (int j = N-1; j >=0; j--)
			{
				 os << num.test(j) ? '1' : '0';
			}



			bool useable = true;

			vector<unsigned> dividers;


			for (int base = 2; base <= 10; base++)
			{

				mpz_int num_in_base;

				mpz_set_str(num_in_base.backend().data(), os.str().c_str(), base);


				//long num_in_base = strtol(os.str().c_str(), NULL, base);

				bool found_divider = false;
				//for (unsigned i = 2; i < ceil(num_in_base/2); i++)
				for (unsigned i = 2; i < 20; i++)
				{
					if (num_in_base % i == 0 && i != num_in_base)
					{
						//cout << " " << num_in_base << "(" << base << ") ";
						found_divider = true;
						dividers.push_back(i);
						break;
					}
				}

				if (!found_divider)
				{
					useable = false;
					break;
				}
			}

			if (useable)
			{
				//cout << "#" << i << " ";
				cout << os.str();


				BOOST_FOREACH(unsigned divider, dividers)
				{
					cout << " " << divider;

				}

				cout << "\n";

				//cout << "\n";

				J--;

				if (J == 0)
				{
					break;
				}
			}



		}



		cout << "\n";
	}

	cout.flush();


	return 0;
}

