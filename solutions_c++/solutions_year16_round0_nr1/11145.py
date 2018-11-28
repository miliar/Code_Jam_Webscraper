
#include<iostream>
#include<fstream>

using namespace std; 

int main()
{
	ifstream input;
	ofstream output;

	input.open("A-large.in");
	output.open("outputfile.txt");


	int originalInput, casesGiven, casesCount = 0;

	input >> casesGiven;

	for (casesCount; casesCount < casesGiven; casesCount++)
	{
		int iterations = 1, Num, alteredNum, checkNum;
		bool tickerA = false, tickerB = false, tickerC = false, tickerD = false, tickerE = false, tickerF = false, tickerG = false, tickerH = false, tickerI = false, tickerJ = false;

		input >> originalInput;
		Num = originalInput;
		alteredNum = Num;

		while (true)
		{ 
			
			if (originalInput == 0)
			{
				output << "Case #" << casesCount + 1 << ": INSOMNIA" << endl;
				break;
			}
			checkNum = alteredNum % 10;

			alteredNum /= 10;				
			
									
			if (checkNum == 0)
			{
				tickerA = true;
			}

			else if (checkNum == 1)
			{
				tickerB = true;
			}

			else if (checkNum == 2)
			{
				tickerC = true;
			}

			else if (checkNum == 3)
			{
				tickerD = true;
			}

			else if (checkNum == 4)
			{
				tickerE = true;
			}

			else if (checkNum == 5)
			{
				tickerF = true;
			}

			else if (checkNum == 6)
			{
				tickerG = true;
			}

			else if (checkNum == 7)
			{
				tickerH = true;
			}

			else if (checkNum == 8)
			{
				tickerI = true;
			}

			else if (checkNum == 9)
			{
				tickerJ = true;
			}	

			if (tickerA == true && tickerB == true && tickerC == true && tickerD == true && tickerE == true && tickerF == true && tickerG == true && tickerH == true && tickerI == true && tickerJ == true)
			{
				output << "Case #" << casesCount + 1 << ": " << Num << endl;
				break;
			}

			if (alteredNum == 0)
			{
				Num = originalInput * iterations;
				alteredNum = Num;
				iterations++;
			}
		}
	}


	input.close();
	output.close();
	return 0;
}
