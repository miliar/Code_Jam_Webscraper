#include "stdafx.h"
#include "CountingSheep.h"
#include <bitset>
void CountingSheep_Start(std::string fname)
{
	std::ifstream infile(fname);
	std::string line;
	std::ofstream ofile("result.txt");


	std::getline(infile, line);
	int tc = 0;
	while (std::getline(infile, line))
	{
		tc++;
		std::istringstream iss(line);

		CountingSheep testObj;

		int value;
		iss >> value;

		int result = testObj.process(value);

		ofile << "Case #" << tc << ": ";
		if (result)
			ofile << result;
		else
			ofile << "INSOMNIA";
		
		ofile << std::endl;

	}
}


int CountingSheep::process(const int value)
{
	//if (value == 0) return 0;

	const int num_mask = std::bitset<16>("1111111111").to_ulong();
	int signer = num_mask;
	int prev_curval = 0;
	int cnt = 1;
	int cur_val;
	

	while (signer)
	{		
		cur_val = cnt * value;
		if (prev_curval == cur_val)
		{
			return 0;
		}
		else
		{
			prev_curval = cur_val;
		}

		while (cur_val)
		{
			int digit_dec = cur_val % 10;
			cur_val = cur_val / 10;

			int digit_bin = (1 << digit_dec);
			int mask_bin = ~digit_bin;

			signer &= mask_bin;

			//std::cout << signer << "mv" << std::hex << digit_bin << std::dec << std::endl;

		}
		++cnt;
	}
	

	return (cnt-1) * value;
}