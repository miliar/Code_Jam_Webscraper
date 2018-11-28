#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

static int numOfTestCases;
static int maxOfShyness;
static string arrOfShyness;



int compute(void)
{
	int fixed=48;
	int totalInitialAudience=0;
	int getAudienceNum;
	int numOfAudienceStoodUp=0;
	int i;
	for(i=0;i<=maxOfShyness;i++)
	{
		getAudienceNum=((int)arrOfShyness[i]-fixed);
		totalInitialAudience+=getAudienceNum;
		if(i==0)
		{
			numOfAudienceStoodUp=getAudienceNum;
		}
		else
		{
			if(numOfAudienceStoodUp>=i)
			{
				numOfAudienceStoodUp+=getAudienceNum;
			}
			else
			{
				int diff=i-numOfAudienceStoodUp;
				numOfAudienceStoodUp=numOfAudienceStoodUp+diff+getAudienceNum;
			}
		}
	}
	return numOfAudienceStoodUp-totalInitialAudience;

}



int main(int argc, char const *argv[])
{
	ifstream fileToOpen("A-large.in");
	ofstream fileToWrite("largeOutput.txt");
	
	fileToOpen>>numOfTestCases;
	int count1=1;

	while(count1<=numOfTestCases)
	{
		fileToOpen>>maxOfShyness;
		fileToOpen>>arrOfShyness;
		fileToWrite<<"Case #"<<count1<<": "<<compute()<<endl;
		count1++;
	}


	fileToOpen.close();
	fileToWrite.close();
}