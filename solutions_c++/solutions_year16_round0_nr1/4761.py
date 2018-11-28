#include <iostream>
#define MAX_NUM 10
using namespace std; 

int CalculateOutput (int numb)
{
	int result = -1;
	if (numb <= 0)	
		return result;	

	bool numberFlags [] = {false, false, false, false, false, false, false, false, false, false};
	int numbNotSee = MAX_NUM;

	int currentNumb;
	int numbTmp = numb;
	int i = 1;
	while (numbNotSee > 0)
	{	
		while (numbTmp > 0)
		{
			currentNumb = numbTmp % 10;		
			numbTmp /= 10;
			if (currentNumb < MAX_NUM && !numberFlags [currentNumb])
			{
				numberFlags [currentNumb] = true;
				numbNotSee--;

				if (numbNotSee <= 0)									
					return numb * i;
			}
		}		

		i++;
		numbTmp = numb * i;		
	}	

	return result;
}

void PrintOutput (int numb, int c)
{
	int result = CalculateOutput (numb);
	 cout << "Case #" << c << ": ";		
	 if (result < 0)
		 cout << "INSOMNIA" << endl;
	 else
		 cout << result << endl;
}

void main() 
{
	int t;					// test case 
	int	N;					// input
	cin >> t; 
	for (int i = 1; i <= t; ++i) 
	{
		cin >> N;  // read N
		PrintOutput (N, i);
	}
}