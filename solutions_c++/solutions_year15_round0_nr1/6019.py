#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#define PROMPT_INCORRECT_INPUT std::cout<<"Incorrect input!"<<std::endl

class Ovation
{
private:
	std::vector<int> SmaxINT;
	std::vector<std::string> SiSTR;
	std::vector<int> ResultINT;

	void PrintResult()
	{
		//std::string ResultString;
		std::vector<int>::iterator it;
		it = ResultINT.begin();

		int Counter = 1;
		for (; it != ResultINT.end(); ++it)
		{
			std::cout << "Case #" << Counter++ << ": " << (*it) << std::endl;
			//ResultString += "Case #" + Counter + ": " + (*it) + "\n";
		}

		//return ResultString;
	}

	void RunStandingOvation()
	{
		// Check input validility first
		// T range
		// 

		if (SmaxINT.size() != SiSTR.size())
		{
			PROMPT_INCORRECT_INPUT;
			return;
		}

		std::vector<int>::iterator it_SmaxINT;
		std::vector<std::string>::iterator it_SiSTR;

		// for (it_SmaxINT = SmaxINT.begin(); it_SmaxINT != SmaxINT.end(); ++it_SmaxINT)
		// {
		// 	std::cout << "Smax: " << (*it_SmaxINT) << std::endl;
		// }
		// for (it_SiSTR = SiSTR.begin(); it_SiSTR != SiSTR.end(); ++it_SiSTR)
		// {
		// 	std::cout << "Si: " << (*it_SiSTR) << std::endl;
		// }

		ResultINT.clear();

		it_SmaxINT = SmaxINT.begin();
		it_SiSTR = SiSTR.begin();

		int i, Smax, InviteNum;
		int ClappingCount;
		std::string Si;
		
		//std::cout << "Smax\tSi" << std::endl;

		for (; it_SmaxINT != SmaxINT.end(); ++it_SmaxINT, ++it_SiSTR)
		{
			//std::cout << (*it_SmaxINT) << "\t" << (*it_SiSTR) << std::endl;
			// Check whether the input can be accessed correctly

			InviteNum = 0;
			ClappingCount = 0;

			Smax = *it_SmaxINT;
			Si = *it_SiSTR;

			for (i = 0; i < Smax + 1; i++)
			{
				ClappingCount += (Si.c_str())[i] - '0';

				if (ClappingCount < i + 1)
				{
					InviteNum += (i + 1) - ClappingCount;
					//std::cout << "Inside 'if': " << InviteNum << std::endl;
					ClappingCount = i + 1;
				}
			}

			ResultINT.push_back(InviteNum);
		}
	}

public:
	Ovation(std::vector<int> Smax, std::vector<std::string> Si){
		this->SmaxINT = Smax;
		this->SiSTR = Si;

		RunStandingOvation();

		PrintResult();
	}
};

int main(int argc, char* argv[])
{
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf

	if (argc < 3)
	{
		std::cout << "PROGRAM INPUT_FILE OUTPUT_FILE" << std::endl;
		return -1;
	}

	std::ifstream in(argv[1]);
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    // std::string line;
    // while(std::getline(std::cin, line))  //input from the file in.txt
    // {
    //     std::cout << line << "\n";   //output to the file out.txt
    // }

    std::ofstream out(argv[2]);
    std::cout.rdbuf(out.rdbuf());
	

	int NumberOfInputs;
	std::cin >> NumberOfInputs;
	//std::cout << "NumberOfInputs: " << NumberOfInputs << std::endl;

	if (NumberOfInputs > 100 || NumberOfInputs < 1)
	{
		//std::cout << "Here" << std::endl;
		PROMPT_INCORRECT_INPUT;
		return -1;
	}

	std::vector<int> Smax;
	std::vector<std::string> Si;

	int Current_Smax = 0;
	std::string Current_Si;
	while (NumberOfInputs--)
	{
		//scanf("%d ", &Current_Smax);
		std::cin >> Current_Smax;
		std::cin >> Current_Si; // Get the current line of input

		Smax.push_back(Current_Smax);
		Si.push_back(Current_Si);
	}

	Ovation SO(Smax, Si);


    std::cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
 
}
