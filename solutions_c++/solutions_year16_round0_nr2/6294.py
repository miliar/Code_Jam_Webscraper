#include "iostream"
#include "fstream"
#include "string"



void main()
{
	std::ifstream input; 
	std::ofstream output;

	input.open("input.txt");
	output.open("output.txt");
	 
	int tes_case; 

	input >> tes_case; 
	int res_out; 
	//subscript begins with zero 
	std::string permu; 
	for (register int i = 1; i <= tes_case; i++)
	{ 
		int current = 0; 
		input >> permu;
		permu += '+'; 
		int size = permu.size() - 2;
		res_out = -1; 
		bool flag = false , lastremnant = false;
		while (true) {
			++res_out; 
			while (true)//finding unidenticallity wow XD
			{
				if (permu[current] != permu[current + 1] && current != size+1) {
					break;
				}
				else if(current == size  && permu[current] == '+')
				{
					flag = true;
					break;
				}
				else
					++current;
			}
			if (permu[current] == '-')
				for (register int iter = 0; iter <= current; iter++)
					permu[iter] = '+';
			else
				for (register int iter = 0; iter <= current; iter++)
					permu[iter] = '-';
			if (flag)
				break; 
			current = 0;
		}
		output << "Case #" << i << ": " << res_out << std::endl; 
	}
}