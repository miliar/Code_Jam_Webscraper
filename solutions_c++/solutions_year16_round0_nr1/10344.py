#include<iostream>
#include<fstream>
#include<map>

int main()
{
	std::ifstream input("D:/A-large (1).in");
	std::ofstream output("D:/googleCodeJam2016ProblemAOutputLarge.txt");
	int T, num;
	input >> T;
	
	for (int numTest = 1; numTest <= T; numTest++)
	{
		input >> num;
		int count = 1;
		std::map<int, bool> digitSeen;
		bool allDigitsSeen = false;

		for (int i = 0; i <= 9; i++)
		{
			digitSeen[i] = false;
		}

		if (num == 0)
		{
			output << "Case #" << numTest << ": INSOMNIA" << std::endl;
		}

		else
		{
			while (!allDigitsSeen)
			{
				for (int i = num*count; i > 0; i /= 10)
				{
					int j = i % 10;
					digitSeen[j] = true;
				}

				allDigitsSeen = true;

				for (int i = 0; i <= 9; i++)
				{
					if (digitSeen[i] == false)
					{
						allDigitsSeen = false;
						count++;
						break;
					}
				}
			}

			output << "Case #" << numTest << ": " << num*count << std::endl;
		}
	}

	return 0;
}