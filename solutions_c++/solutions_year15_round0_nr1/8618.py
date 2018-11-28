#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
using namespace std;

void StandingOvation(void);

int main()
{
	StandingOvation();

	return 0;
}


void StandingOvation(void)
{
	string sLine;
	ifstream  inf;
	int nCases = 0;
	int nShyMax = 0;
	long nSum=0, nCount=0;

	inf.open("D:/Geek/POWER_SCS/Workspaces/WindowsIDE/GoogleCodejam/Files/StandingOvation/A-large.in");
	if(!inf.is_open())
	{
		cout<<"something wrong with the input file"<<endl;
		return;
	}

	ofstream outf;
	outf.open("D:/Geek/POWER_SCS/Workspaces/WindowsIDE/GoogleCodejam/Files/StandingOvation/A-largeOutput.out");

	//Read Input 
	inf >> nCases;
	for(int irow=1; irow <= nCases; irow++)
	{
		nShyMax = nSum = nCount = 0;
		inf >> nShyMax >> sLine;

		for(int icol =0; icol<=nShyMax;icol++)
		{
			if(icol==0)
			{
				nSum += atoi(sLine.substr(icol, 1).c_str());
			}
			else
			{
				if(nSum >= icol)
				{
					nSum += atoi(sLine.substr(icol, 1).c_str());
				}
				else
				{
					nCount++;
					nSum++;
					nSum += atoi(sLine.substr(icol, 1).c_str());
				}
			}

			if(nSum>=nShyMax)
				break;
		}

		//Print Output
		outf << "Case #" << irow << ": " << nCount << '\n';

	}// do for no of cases
}
