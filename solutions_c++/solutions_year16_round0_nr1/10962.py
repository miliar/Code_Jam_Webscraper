#include<iostream>
#include<fstream>
#include<stdbool.h>

using namespace std;

bool seenDigitsList[10];
int calcLastNumberFrom(int);

int main(int argc,char *argv[])
{
	ifstream inf(argv[1]);
	int testCases=9,choosenNumber,lastNumber,i;
	inf>>testCases;

	for(i=0;i<testCases;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		
		inf>>choosenNumber;
		if(choosenNumber==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		lastNumber=calcLastNumberFrom(choosenNumber);
		cout<<lastNumber<<endl;
		
		/*for(int a=987654;a!=0;a/=10)
		{
			cout<<a%10<<endl;
		}*///for testing only
	}

return 0;
}

int calcLastNumberFrom(int seed)
{
	int lastNumber=0,nextSeed;
	int checkSeen;
	
	for(int i=0;i<10;i++)
	{
		seenDigitsList[i]=false;
	}//falsifies all "seen"s
	
	for(int n=1;;n++)
	{
		for(nextSeed=n*seed;nextSeed!=0;nextSeed/=10)
		{
			seenDigitsList[nextSeed%10]=true;
		}//marks digits seen in nextSeed
	
		for(checkSeen=0;checkSeen<10;checkSeen++)
		{
			if(seenDigitsList[checkSeen]==false)
				break;
			else
				continue;
		}
	
		if(checkSeen==10)
		{
			lastNumber=n*seed;
			break;
		}
		else
		{
			checkSeen=0;
			continue;
		}
	}
		
	return lastNumber;
}
