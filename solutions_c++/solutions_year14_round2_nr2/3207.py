#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <bitset>

std::ofstream writer("C:\\Users\\Dave\\Documents\\Code Jam\\2014\\Round1B\\B-output.out");
std::ifstream reader ("C:\\Users\\Dave\\Downloads\\B-small-attempt1.in");

std::bitset<64> Number1;
std::bitset<64> Number2;
std::bitset<64> Number3;
std::bitset<64> WinningNumber;

unsigned long long binaryToDecimal(std::string number)
{
    unsigned long long result = 0;
	int pow = 1;
    for (int i = number.length() - 1; i >= 0; --i, pow <<= 1 )
	{
        result += (number[i] - '0') * pow;
	}
    return result;
}

int main()
{
	//T number of test cases

	int T = 0;
	unsigned long long A = 0;
	unsigned long long B = 0;
	unsigned long  long K = 0;

	if (!writer)
	{
		std::cout << "Error opening file for output" << std::endl;
		return -1;
	}

	if (!reader)
	{
		std::cout << "Error opening file for input" << std::endl;
		return -1;
	}

	reader >> T;

	for(int i=0;i<T;i++)
	{
		writer << "Case #" << i + 1 << ": ";
		reader >> A;
		reader >> B;
		reader >> K;

		//Number3 = K;

		unsigned long long WinNo;
		std::string WinNoString;
		int Counter = 0;

		for(int x=0;x<A;x++)
		{
			//Number1 = x;
			for(int y=0;y<B;y++)
			{
				WinNo = x & y;
				//Number2 = y;
				//WinningNumber = (Number1&Number2);
				//WinNoString = WinningNumber.to_string<char,std::string::traits_type,std::string::allocator_type>();
				//WinNo = binaryToDecimal(WinNoString);
				if(WinNo < K)
				{
					Counter = Counter +1;
				}
			}
		}

		writer << Counter << std::endl;
	}

	
	reader.close();
	writer.close();

	return 0;
}