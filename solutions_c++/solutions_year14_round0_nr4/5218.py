#include<iostream>
#include<fstream>
#include <vector>
#include<algorithm>
#include <deque>
#include <stdlib.h>

using namespace std;

deque <int> Ken, Naomi;
int T,n;
ifstream fin("input.txt");
ofstream fout("output.txt");

void readInputdata()
{
	ifstream fin("input.txt");
}

void initData()
{

	fin>>T;
}

void readInput()
{

	fin>>n;
	int aux;
	char line[8000];

		fin.getline(line,10);
		line[0] ='\0';
		fin.getline(line,8000); 
		char *nr = strtok(line," ");
		while(nr)
		{
			Naomi.push_back(atoi(&nr[2]));
			nr = strtok(NULL, " ");
		}
		line[0] ='\0';

		sort(Naomi.begin(),Naomi.end());
	    

		fin.getline(line,8000); 
		nr = strtok(line," ");
		while(nr)
		{
			Ken.push_back(atoi(&nr[2]));
			nr = strtok(NULL, " ");
		}

		line[0] ='\0';
		
		sort(Ken.begin(), Ken.end());
}

void resetInput()
{
	Naomi.clear();
	Ken.clear();
}

void printOutput(int caseInd, int naomiPoints, int kenPoints)
{
	fout<<"Case #"<<caseInd<<": "<<naomiPoints<<" "<<kenPoints<<"\n";
}
void solveProblem()
{
	
	for(int i = 1; i <= T; i++)
	{
		int naomiPointsW = 0, naomiPointsD = 0;
        readInput();
		deque <int> kenC(Ken), naomiC(Naomi);
		int len = n;

		while(len)
		{
			if( Naomi.front() > Ken.front())
			{
				++naomiPointsD;
				Ken.pop_front();		
			}else
				Ken.pop_back();

             Naomi.pop_front();
			 --len;
				
		}
		
		len = n;

		while(len)
		{
			deque<int>::iterator it;

			if( naomiC.front() > kenC.back())
				{
					kenC.pop_front();
					++naomiPointsW;
				} else
				  {
					  it = kenC.begin();
					  while(*it < naomiC.front())
						   ++it;
					  kenC.erase(it);

				   }
				naomiC.pop_front();
				--len;

		}
		printOutput(i,naomiPointsD,naomiPointsW);
		resetInput();
	}
}


int main()
{
	initData();
	solveProblem();
	return 0;
}