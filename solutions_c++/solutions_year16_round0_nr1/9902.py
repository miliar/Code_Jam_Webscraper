#include <iostream>
#include <string>

#define LOOP_LIMIT 100000000

using namespace std;
int main()
{
		int numCases;
		string inString;
		cin >> numCases;
		getline(cin, inString); //flush the line
		for(int i = 0; i < numCases; i++) //loop through the cases
		{
				cout << "Case #" << i+1 << ": ";
				int numToCountFrom;
				cin >> numToCountFrom;
				int multiplier = 0;
				bool awake = true;
				int numLoops = 0;
				bool digitsFound[10];
				for(int j = 0; j < 10; j++)
				{
						digitsFound[j] = false;
				}
				while(awake && numLoops < LOOP_LIMIT)
				{
						numLoops++;
						multiplier++;
						int currentNum = numToCountFrom * multiplier;
						int digit = 1;
						while(digit <= currentNum)
						{
							int currDigit = currentNum / digit % 10;
							digitsFound[currDigit] = true;
							digit *= 10;
						}	
						bool allFound = true;
						for(int j = 0; j < 10; j++)
						{
							if(!digitsFound[j])
									allFound = false;
						}
						if(allFound)
						{
								awake = false;
								cout << currentNum << endl;
						}
				}
				if(numLoops == LOOP_LIMIT)
				{
						cout << "INSOMNIA" << endl;
				}
		}
		return 0;
}
