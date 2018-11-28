#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ifstream infile ("A-large.in");
	std::ofstream outfile ("sheep_out_b.txt", std::ofstream::out);
	int numCases;
	int start, current, digit, track;
	int check[10];
	
	if (infile.is_open())
    {
    	infile >> numCases;
    	for (int i = 0; i < numCases; ++i)
    	{
    		infile >> start;
    		for (int j = 0; j < 10; ++j)
    			{
    				check[j] = 0;
    			}
    		digit = 0;
    		track = 0;
    		while (start <= 1000000 && start > 0 && digit !=10)
    		{
    			track += 1;
    			current = start * track;
    			while (current !=0)
    			{
    				digit = current % 10;
    				check[digit] = 1;
    				current = current / 10;
    			}
    			digit = 0;
    			for (int j = 0; j < 10; ++j)
    			{
    				digit += check[j];
    			}
    			if (digit == 10)
    			{
    				outfile << "Case #" << i + 1 << ": " << start * track << std::endl;
    			}
    		}
    		if (digit < 10)
    		{
    			outfile << "Case #" << i + 1 << ": " <<"INSOMNIA" << std::endl;
    		}
    	}
    }
    infile.close();
    outfile.close();
	return 0;
}