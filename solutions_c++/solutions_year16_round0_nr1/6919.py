#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	
	int CheckArray[10] = {0};
	
	ifstream myIn;
	myIn.open("C:\\Users\\Simeon\\Downloads\\A-large.in");
	ofstream MyOut;
	MyOut.open("C:\\Users\\Simeon\\Documents\\CODING\\Project1\\Project1A-LARGE-solutionFINAL.txt");
	
	long input = 0;

	myIn >> input;
	for(int i = 0; i < input; i++)
	{
		long numberTEST = 0;
		long TOTAL = 0;
		long number2 = 0;
		long numberx = 0;
		myIn >> numberx;
		

	for(int a = 1; a <= 1000; a++)
	{

		bool check = false;

		
		if(number2 == 0)
		number2 = numberx;
		else
			number2 = number2 + numberx;
		TOTAL = number2;
		
		if(number2 < 10)
		{
			CheckArray[number2] = true;
		}
		else if(number2 < 100)
		{
			CheckArray[(number2 % 10)]++;
			CheckArray[(number2 / 10)]++;
		}
		else if(number2 < 1000)
		{
			long temp = 0;
			CheckArray[(number2 / 100)]++;
			temp = number2 % 100;
			CheckArray[(temp / 10)]++;
			temp = (number2 % 100) % 10;
			CheckArray[temp]++;
		}
		else if(number2 < 10000)
		{
			long temp = 0;
			CheckArray[(number2 / 1000)]++;
			temp = number2 % 1000;
			CheckArray[(temp / 100)]++;
			temp = (number2 % 100);
			CheckArray[temp / 10]++;
			temp = ( number2 % 10);
			CheckArray[temp]++;
		}
		else if(number2 < 100000)
		{
			long temp = 0;
			CheckArray[(number2 / 10000)]++;
			temp = number2 % 10000;
			CheckArray[(temp / 1000)]++;
			temp = (number2 % 1000);
			CheckArray[temp / 100]++;
			temp = ( number2 % 100);
			CheckArray[temp / 10]++;
			temp = ( number2 % 10);
			CheckArray[temp]++;
		}
		else if(number2 < 1000000)
		{
			long temp = 0;
			CheckArray[(number2 / 100000)]++; 
			temp = number2 % 100000; 
			CheckArray[(temp / 10000)]++; 
			temp = (number2 % 10000); 
			CheckArray[temp / 1000]++; 
			temp = ( number2 % 1000); 
			CheckArray[temp / 100]++; 
			temp = ( number2 % 100); 
			CheckArray[temp / 10]++; 
			temp = ( number2 % 10); 
			CheckArray[temp]++;
		}
		else if(number2 < 10000000)
		{
			long temp = 0;
			CheckArray[(number2 / 1000000)]++; 
			temp = number2 % 1000000; 
			CheckArray[(temp / 100000)]++; 
			temp = (number2 % 100000); 
			CheckArray[temp / 10000]++; 
			temp = ( number2 % 10000); 
			CheckArray[temp / 1000]++; 
			temp = ( number2 % 1000); 
			CheckArray[temp / 100]++; 
			temp = ( number2 % 100); 
			CheckArray[temp / 10]++; 
			temp = ( number2 % 10); 
			CheckArray[temp]++;
		}
		else
		{
			long temp = 0;
			CheckArray[(number2 / 10000000)]++; 
			temp = number2 % 10000000; 
			CheckArray[(temp / 1000000)]++; 
			temp = (number2 % 1000000); 
			CheckArray[temp / 100000]++; 
			temp = ( number2 % 100000); 
			CheckArray[temp / 10000]++; 
			temp = ( number2 % 10000); 
			CheckArray[temp / 1000]++; 
			temp = ( number2 % 1000); 
			CheckArray[temp / 100]++; 
			temp = ( number2 % 100); 
			CheckArray[temp / 10]++; 
			temp = ( number2 % 10); 
			CheckArray[temp]++;
		}

		int count = 0;
		for(int i = 0; i < 10; i++)
		{
			if(CheckArray[i] > 0)
				count++;
			if(count == 10)
				check = true;
	
		}
		if(check == true)
		{
			for(int lol = 0; lol < 10; lol++)
			{
				CheckArray[lol] = 0;
			}
		numberTEST = number2;
		break;
		}
		
	  } // inner for

	if(numberTEST != 0)
	MyOut << "Case #" << i+1 << ": " << numberTEST << endl;
	else
	{
		MyOut << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		for(int lol = 0; lol < 10; lol++)
			{
				CheckArray[lol] = 0;
			}
	}

	} // outer for 
	return 0;
}

