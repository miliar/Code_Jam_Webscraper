#include "stdafx.h"
#include "PancakeRevenge.h"

void PancakeRevenge_Start(std::string fname)
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

		PancakeRevenge testObj;

		std::string q;
		iss >> q;
				
		ofile << "Case #" << tc << ": " << testObj.process(q) << std::endl;

	}
}

int PancakeRevenge::process(std::string str)
{
	std::string str_rev(str.rbegin(),str.rend());
	const char* c_buff = str_rev.c_str();
	int cnt = 0;
	
	while (c_buff[cnt] != 0)
	{
		add( (Face) (c_buff[cnt]));
		cnt++;
	}
	
	return flips();
}

void PancakeRevenge::add(Face f)
{
	if (pancakes.empty() || pancakes.top() != f)
		pancakes.push(f);
}

int PancakeRevenge::flips()
{
	int flip_cnt = 0;
	while ( (false == pancakes.empty() ) )
	{
		if (pancakes.top() == HAPPY && pancakes.size() > 1)
		{//flip:2 pop:2			
			pancakes.pop();
			flip_cnt++;

			pancakes.pop();
			flip_cnt++;
		}
		else if (pancakes.top() == BLANK)
		{//pop:1 flip:1
			pancakes.pop();
			flip_cnt++;
		}
		else
		{
			pancakes.pop();
		}


	}

	return flip_cnt;
}
