#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool checkInput(char inStr[],int len)
{
	for(int i=0;i<len;i++)
	{
		if(inStr[i]=='-')
			return false;
	}
	return true;
}

int main()
{
	ifstream infile("file2.in");
	ofstream outfile("file2.out");
	int T,t = 1;
	infile>>T;
	while(t<=T)
	{
		string N;
		infile>>N;
		int strLen = N.length();
		char curInput[strLen];
		strcpy(curInput,N.c_str());
		int resCount = 1;
		int flag;

		if(strLen==1)
		{
			if(curInput[0]=='+')
				outfile<<"Case #"<<t<<": "<<"0"<<endl;
			else
				outfile<<"Case #"<<t<<": "<<resCount<<endl;
			flag = 0;
		}
		for(int i=0;i<strLen-1;i++)
		{
			int j=i+1;
		    flag = 1;
			if(checkInput(curInput,strLen))
			{
				outfile<<"Case #"<<t<<": "<<"0"<<endl;
				flag = 0;
				break;
			}

			if(curInput[i]!=curInput[j])
			{
				if(!(curInput[i]=='-' && i==0))
					resCount++;
			}
		}

		if(curInput[strLen-1]=='+' && curInput[strLen-2]=='-')
		 	resCount--;
		if(flag)
			outfile<<"Case #"<<t<<": "<<resCount<<endl;
		t++;
	}
}