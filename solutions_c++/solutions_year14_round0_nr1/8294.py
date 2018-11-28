#include <iostream>
#include <string>

const std::string SBAD = "Bad magician!";
const std::string SCHEATED = "Volunteer cheated!";

const unsigned int CORRECT = 0;
const unsigned int BAD = 1;
const unsigned int CHEATED = 2;

int main(void)
{
	std::string _str;
	unsigned int tc = 0;
	std::cin >> tc;
	
	for(unsigned int i=0; i<tc; i++)
	{
		unsigned int arr1_row=0, arr2_row=0;
		unsigned int arr1[4]={0}, arr2[4]={0}, dump[4] = {0};
		
		std::cin >> arr1_row;
		
		for(int c=0; c<4; c++)
			if(arr1_row == (c+1))
				std::cin >> arr1[0] >> arr1[1] >> arr1[2] >> arr1[3];
			else
				std::cin >> dump[0] >> dump[1] >> dump[2] >> dump[3];
		
		std::cin >> arr2_row;
		
		for(int c=0; c<4; c++)
			if(arr2_row == (c+1))
				std::cin >> arr2[0] >> arr2[1] >> arr2[2] >> arr2[3];
			else
				std::cin >> dump[0] >> dump[1] >> dump[2] >> dump[3];
		
		unsigned int state = CORRECT;
		
		unsigned int correct = 0;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if(arr1[j] == arr2[k])
				{
					if(correct == 0)
						correct = arr1[j];
					else
					{
						state = BAD;
						break;
					}
				}
				
			}
			
			if(state == BAD)
				break;
		}
		
		if(correct == 0)
			state = CHEATED;
		
		if(state != CORRECT)
			std::cout << "Case #" << i+1 << ": " << (state == BAD ? SBAD : SCHEATED) << std::endl;
		else
			std::cout << "Case #" << i+1 << ": " << correct << std::endl;
	}
	
	return 0;
}