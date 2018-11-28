#include <iostream>
#include <string.h>
using namespace std;

int checkForSuccess(char *str, int strLen)
{
	while(--strLen>=0 && str[strLen] =='+' );

	if(strLen == -1)
	{
		return 1;
	}
	else
		return 0;
}

void flipCakes(char *p, int strLen, int flipNo)
{
	char temp[101];
	int cpyFlipNo = flipNo;

	//make a copy in temp
	for(int k=0; k<=strLen;k++)
	{
		temp[k] = p[k];
	}

	for(int k=0;k<flipNo;k++)
	{
		p[k] = temp[--cpyFlipNo]=='+'?'-':'+';
	}

	//flipped
}

int main()
{
	
	char input[101];
	unsigned int testCases=0,i=0,iterations=0; 
	int success=0, strLength=0;
	cin>> testCases;

	
	
	while(testCases--)
	{
		i++;
		iterations = 0;
		success= 0;
		strLength = 0;
		cin>>input;
		strLength = strlen(input);
		success = checkForSuccess(input,strLength);
		if(success)
		{
			cout<<"Case #"<<i<<": "<<iterations<<endl;
			continue;
		}

		while(!success)
		{
			char cur = input[0];
			char prev = input[0];
			int k=1;

			for(k=1;k<strLength;k++)
			{
				if(input[k] != prev)
				{
					break;
				}
				prev=input[k];
			}

			flipCakes(input,strLength,k);
			iterations++;
			success = checkForSuccess(input,strLength);
			if(success)
			{
				cout<<"Case #"<<i<<": "<<iterations<<endl;
			}

		}
	


	}


	//find out consecutive same sides before different side encounter or end of stack encounter
	//flip these same sides
	//check if we have succeded, if not repeat

	
	
	return 0;

}