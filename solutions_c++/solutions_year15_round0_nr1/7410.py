#include "StandingOvation.h"

StandingOvation::StandingOvation(void)
{
}

StandingOvation::~StandingOvation(void)
{
}


int StandingOvation::Solve(CHAR_BUFFER shyness, int size)
{
	if(size == 1)
	{
		return 0;
	}

	int personStanding = (shyness[0] - '0');
	int itr = 1;
	int personNeeded = 0;

	while(itr < size)
	{
		int numPerson = (shyness[itr] - '0');
		int existingVirtualPStanding = personStanding + personNeeded;

		if(numPerson > 0)
		{
			if(existingVirtualPStanding < itr)
			{
				personNeeded += (itr - existingVirtualPStanding);
			}
		}

		personStanding += numPerson;
		
		itr++;
	};

	return personNeeded;
}


void StandingOvation::Test()
{
	//std::ifstream inputFile("A-small-practice.in");
	std::ifstream inputFile("A-large-practice.in");
	std::ofstream outputFile("output.txt", std::ios::app);

	if(inputFile.is_open())
	{
		int maxShy = 0;
		int NT = 0;
		inputFile>>NT;

		StandingOvation so;
		for(int t = 0; t < NT; t++)
		{
			inputFile>>maxShy;

			CHAR_BUFFER buff = new char[maxShy + 1];
			for(int i = 0; i <= maxShy; i++)
			{
				inputFile>>buff[i];
			}

			int numneeded = so.Solve(buff, maxShy + 1);
			std::cout<<"Case #"<<t + 1<<": "<<numneeded<<std::endl;;
			outputFile<<"Case #"<<t + 1<<": "<<numneeded<<std::endl;;
		}
	}
}