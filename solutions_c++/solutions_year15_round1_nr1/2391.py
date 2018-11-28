#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <bitset>


int main(char * argc,int argv)
{
	std::ifstream file_input("data.in", std::ifstream::in);
	std::ofstream file_output("data.out", std::ofstream::out);
	long long int n_tests = 0;
	file_input >> n_tests;
	for (long long int iter1 = 0; iter1 < n_tests; iter1 += 1)
	{
		int result1 = 0;
		int result2 = 0;
		std::vector<int> eat_list;
		int n_snaps = 0;
		file_input >> n_snaps;
		int rate = 0;
		for(int iter2 = 0; iter2 < n_snaps; iter2++)
		{
			int n_eaten = 0;
			file_input >> n_eaten;
			if(iter2 != 0 && rate < (eat_list.back() - n_eaten))
			{
				rate = eat_list.back() - n_eaten;
			}
			eat_list.push_back(n_eaten);
			
		}	

		std::vector<int>::iterator it;
		int prev_cnt = 0;
		for(it = eat_list.begin();it != eat_list.end(); it++)
		{
			
			if(prev_cnt > *it)
			{
				result1 += (prev_cnt - *it);
			}

			if(*it < rate)
			{
				if(it != --eat_list.end())
				{
				result2 += *it;
				}
			}
			else
			{
				if(it != --eat_list.end())
				{
				result2 += rate;
				}
			}
			prev_cnt = *it;
		}
		file_output << "Case #" << (iter1 + 1) << ": " << result1 << " " << result2 << std::endl;
	}
	return(1);
}