#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream in("dummyInput.in");
	ofstream out("dummy.out");
	int cases  = 0;
	int currentCase = 1;
	int firstResponse = 0;
	int secondResponse = 0;
	int firstRow[4];
	int secondRow[4];
	int dummy = 0;
	int currentLine = 1;

	int responseType = 0;
	int answer;

	if(in.is_open())
	{
		in>>cases;
		while(currentCase <= cases)
		{

			//Getting Volunteer's Answered Rows

			in>>firstResponse;
			cout<<firstResponse<<endl;
			while(currentLine <= 4)
			{
				for(int i=0;i<4;i++)
				{
					
					if(currentLine == firstResponse)					
						in>>firstRow[i];
					else
						in>>dummy;
									
				}
				currentLine++;
			}	

			

			currentLine = 1;		//Resetting currentLine Variable

			in>>secondResponse;
			cout<<secondResponse<<endl;
			while(currentLine <= 4)
			{
				for(int i=0;i<4;i++)
				{
					
					if(currentLine == secondResponse)
						in>>secondRow[i];	
					else
						in>>dummy;								
				}
				currentLine++;
			}	


			//Finding the output from Both Rows
			responseType = 0;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
				
					if((firstRow[i] == secondRow[j]) && (responseType == 0))
					{
						answer = firstRow[i];
						responseType = 1;					
					}
					else if((firstRow[i] == secondRow[j]) && (responseType == 1))
					{
						responseType = 2;				
					}
						
				}			
			}

			//Printing Result on Output File
			
			if(responseType == 0)
				out<<"Case #"<<currentCase<<": "<<"Volunteer cheated!"<<endl;
			else if(responseType == 1)
				out<<"Case #"<<currentCase<<": "<<answer<<endl;
			else if(responseType == 2)
				out<<"Case #"<<currentCase<<": "<<"Bad magician!"<<endl;
			
			//Reseting Variables
			currentLine = 1;
			currentCase++;

		}	
	}

	in.close();
}
