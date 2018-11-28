#include<iostream>
#include<string>
#include<fstream>

using namespace std;

void main()
{
	int noOfTestCases;
	int testCaseIndex=1;
	string inputLine;
	//Read input file
	ifstream inputFile ("input.in");
	//Write output file
	ofstream outputFile ("output.txt");

	if((inputFile.is_open() && outputFile.is_open()))
	{
		int lineIndex=0;
		while(! inputFile.eof())
		{
			getline(inputFile,inputLine);
			if(lineIndex==0)//first line of the input indicates no. of testcases
				noOfTestCases=stoi(inputLine);
			else if(lineIndex==(noOfTestCases+1))
				;//do nothing in case of an extra (empty) line at the end of the input file {to avoid exceptions}
			else//nth line of the input indicates the nth test case where n!=0 (not the first line)
				{
					int requiredNoOfInvitedFriends=0;
					int maxShynessLevel=stoi(inputLine.substr(0,inputLine.find(" "))); //first number of the nth line indicates the maximum shyness level of the audience
					string shynessLevelCountOfAudience= inputLine.substr(inputLine.find(" ")+1);
					for(int i=1 ; i<=maxShynessLevel ; i++)
					{
						int countOfAudienceWhoWillStandBeforeMe=0;
						for(int j=0 ; j<i; j++)
							countOfAudienceWhoWillStandBeforeMe += (shynessLevelCountOfAudience[j]-'0');
						if ((countOfAudienceWhoWillStandBeforeMe + requiredNoOfInvitedFriends) < i)
							requiredNoOfInvitedFriends += (i - countOfAudienceWhoWillStandBeforeMe - requiredNoOfInvitedFriends);
					}
					
					outputFile<<"Case #"<<(testCaseIndex++)<<": "<<requiredNoOfInvitedFriends<<endl;
				}
			lineIndex++;
		}
	}
	
}