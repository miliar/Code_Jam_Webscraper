#include <iostream>
#include <climits>
#include <fstream>

using namespace std;

int main()
{
ifstream inFile;
inFile.open("A-large.in");
ofstream outFile;
outFile.open("Output.txt");
long testCases = 0;
long n = 0;
long result;
long saveResult;
bool trackDigits[10];
bool allDigits = false;
long digit;
long counter;

inFile >> testCases;

for(int z = 0; z < 10; z++)
{
	trackDigits[z] = false;
}

//Test Case
for(int i =0; i < testCases; i++)
{
    counter = 1;
	//get Input;
	inFile >> n;
	//cout << n;
    result = 1;
	while(allDigits == false && n != 0)
	{
	    result = n*counter;
        //cout << result << endl;
        saveResult = result;
        counter++;

        while(result > 0 && allDigits == false)
		{
			digit = result%10;
            result = result/10;
            //cout << digit << endl;
			switch(digit)
			{
				case 0: trackDigits[0] = true;
						break;
				case 1: trackDigits[1] = true;
						break;
				case 2: trackDigits[2] = true;
						break;
				case 3: trackDigits[3] = true;
						break;
				case 4: trackDigits[4] = true;
						break;
				case 5: trackDigits[5] = true;
						break;
				case 6: trackDigits[6] = true;
						break;
				case 7: trackDigits[7] = true;
						break;
				case 8: trackDigits[8] = true;
						break;
				case 9: trackDigits[9] = true;
						break;
				default: ;
			}
			allDigits = true;
			for(int z = 0; z < 10; z++)
			{
				if(trackDigits[z] == false)
				{
					z = 10;
					allDigits = false;
				}
			}

		}

	}

	if(allDigits == true)
	{
		outFile << "Case #" << i+1 << ": " << saveResult << endl;
		allDigits = false;
		for(int z = 0; z < 10; z++)
        {
            trackDigits[z] = false;
        }
	}

	else
	{
		outFile << "Case #" << i+1 << ": INSOMNIA" << endl;
		allDigits = false;
		for(int z = 0; z < 10; z++)
        {
            trackDigits[z] = false;
        }
	}





}


inFile.close();
outFile.close();


return 0;
}
