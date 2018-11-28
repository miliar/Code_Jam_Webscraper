#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int writeSummary(int start, int end);
int reverseDirection(int num);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		int start = 0;
		int end = 0;
		myfileIn >> start;
		myfileIn >> end;

		myfileOut << "Case #" << (i+1) << ": " << writeSummary(start, end) << endl;
		cout << "Case #" << (i+1) << ": " << writeSummary(start, end) << endl;
	}

	return 0;
}

int writeSummary(int start, int end)
{
	int qualify = 0;
	for(int i = start; i <= end; i++)
	{
		if(i == reverseDirection(i))
		{
			double answer = sqrt((double)i);
			if(answer == (int)answer)
			{
				if(answer == reverseDirection((int)answer))
				{
					qualify++;
				}
			}
		}
	}
	return qualify;
}

int reverseDirection(int num)
{
	if(num < 10)
	{
		return num;
	}
	int digits = 1;
	while(num > (num%digits))
	{
		digits *= 10;
	}
	return ((digits/10)*(num%10))+reverseDirection(num/10);
}