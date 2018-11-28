#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


const bool OUTPUT_TO_FILE = true;


string beginning_of_ans(int n, pair<int, int> p1, pair<int, int> p2)
{
	char jamcoin[n];
	for (int i = 0; i < n; i++)
	{
		jamcoin[i] = '0';
	}
	jamcoin[0] = '1';
	jamcoin[n - 1] = '1';
	jamcoin[2*p1.first + 1] = '1';
	jamcoin[2*p1.second + 1] = '1';
	jamcoin[2*p2.first + 2] = '1';
	jamcoin[2*p2.second + 2] = '1';

	string ret(jamcoin);
	return ret;
}

pair<int, int> get_comb(int num_of_positions, int comb_idx)
{
	int counter = comb_idx;
	int last_idx = num_of_positions - 1;
	pair<int, int> val;
	val.first = 0;
	val.second = 1;

	int diff;
	while (true)
	{
		diff = last_idx - val.second;
		counter -= diff;
		if (counter <= 0)
		{
			diff += counter;
			val.second += diff;
			break;
		}
		counter--;
		val.first++;
		val.second = val.first + 1;
	}

	return val;
}


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	int t;
	int n;
	int j;

	string partial_ans = " 3 2 3 2 7 2 3 2 3\n";
	int num_of_positions;
	int combs;
	int comb_1;
	int comb_2;
	pair<int, int> pair_1;
	pair<int, int> pair_2;

	cin >> t;
	cin >> n >> j;
	output << "Case #1:\n";

	num_of_positions = (n - 2)/2;
	combs = num_of_positions*(num_of_positions - 1)/2;

	for (int i = 0; i < j; i++)
	{
		comb_1 = i % combs;
		comb_2 = i / combs;

		pair_1 = get_comb(num_of_positions, comb_1);
		pair_2 = get_comb(num_of_positions, comb_2);

		output << beginning_of_ans(n, pair_1, pair_2) + partial_ans;
	}


	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
