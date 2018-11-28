#include "iostream"
#include "fstream"



void main()
{
	std::ifstream input; 
	std::ofstream output;

	input.open("input.txt");
	output.open("output.txt");
	 
	int tes_case; 

	input >> tes_case; 
	int N, onworking , res_out = 1 ; 

	
	for (register int i = 1; i <= tes_case; i++)
	{
		bool check_out[10]{ false };
		bool flag_insomnia = false; 
		res_out = 1; 
		input >> N; 
		if (N != 0) {
			flag_insomnia = true;
			while (true) {
				onworking = N*res_out;
				while (onworking != 0 ) //for import the digits ... 
				{
					int temp; 
					temp = onworking;
					onworking /= 10; //integer dividing 
					onworking *= 10; 
					check_out[temp-onworking]=true;
					onworking /= 10;
				}
				bool flag = false;
				for (register int j = 0; j <= 9; j++) {
					if (check_out[j] == false) {
						flag = true;
						break;
					}
				}
				if (flag == true) {
					++res_out;
				}
				else break; 
			}
		}
		if (flag_insomnia == false)
			output << "Case #" << i << ": " << "INSOMNIA" << std::endl;
		else
			output << "Case #" << i << ": " << res_out*N << std::endl; 
	}

}