#include <iostream>
using namespace std;

int testInsomnia(long int num){
	if(!num)
	{
		return -1;
	}

	return 0;
}

int main()
{
	int testCases=0;
	long int N;
	int i=1;
	int insomnia;
	//int arUnits[10] = {0,0,0,0,0,0,0,0,0,0};
	long int temp, inc;
	int compFlag;
	//getting no of test cases
	cin>>testCases;

	while(testCases--)
	{
		cin>>N;
		insomnia = testInsomnia(N);
		if(insomnia <0)
		{
			cout<<"Case #"<<i++<<": INSOMNIA"<<endl;
			continue;
		}
		temp = N;
		compFlag = 0;
		inc = 1;
		int arUnits[10] = {0,0,0,0,0,0,0,0,0,0};
		while(!compFlag)
		{
			//temp=N;
			while(temp)
			{
				long int rem = temp%10;
				arUnits[rem] = 1;
				temp=temp/10;
			}

			compFlag = 1;
			for(int j=0; j<10;j++)
			{
				if(!arUnits[j])
				{
					compFlag = 0;
					break;
				}
			}

			if(!compFlag)
			{
				temp = N*(++inc);
			}
			else
			{
				cout<<"Case #"<<i++<<": "<<N*inc<<endl;		
			}

		}

	}

	return 0;
}