#include <iostream>
#include <string>
#include <list>
#include <vector>

using namespace std;

void ReadCases( list<int>& oNumbers, int& oCount )
{
	int number;
	cin >> oCount;
	for( int i = 0; i < oCount; ++i )
	{
		cin >> number;
		oNumbers.push_back(number);
	}
}

void Output(int iIndex, int iResult )//iResult[]
{
	//for( int i = 0; i < iCount; ++i )
	{
		string temp = to_string(static_cast<unsigned long long>(iResult));
		cout << "Case #" << iIndex << ": " << ( (iResult == 0) ? "INSOMNIA" : temp) << endl;
	}
}

void SplitNumber(vector<int>& oDigits, int& oCount, int iNumber) {
	if (0 == iNumber) { 
		oDigits.push_back(0);
	} else {
		while (iNumber != 0) {
			int last = iNumber % 10;
			oDigits.push_back(last);	//The first element is the least significant digit 
			++oCount;
			iNumber = (iNumber - last) / 10;
		}
	}
}

//create a pointer for each digit in the number
//2*N = N+N
//so just move the pointer by the setp of the digit to do the calculation
//p0 is the 0 digit, and its value is which digit (0-9) it currently points at
int CountNumbers(int iNumber)
{
	bool counted[10] = {false};	//the index is the number, the value shows if it has been counted
	vector<int> digits;
	int count = 0;
	SplitNumber(digits, count, iNumber);

	int CountedNumbers = 0;

	//pointers of digits in the number

	vector<int> pDigits;
	for( int i = 0; i < count; ++i )
	{
		pDigits.push_back(0);
	}

	bool changed = false;	//check if the pointers are changed in one traverse. 
							//If it is not changed, we will never get the result

	int k = 0; //return k*N
	while( 10!= CountedNumbers )
	{
		//traverse from the least significant digit to the highest one
		//The first element is the least significant digit
		//int pointercount = 0;
		for ( int i = 0; i < pDigits.size(); ++i )
		{
			int tempPointer = pDigits[i];
			if( i < digits.size() )
			{
				tempPointer += digits[i];	//move digits[i] steps
				tempPointer %= 10;
			}
			
			//carry
			if(tempPointer<pDigits[i] )
			{
				if( i == pDigits.size()-1)
				{
					pDigits.push_back(0);
				}
				pDigits[i+1]+=1;	//carry
			}

			if( tempPointer != pDigits[i] )
			{
				changed = true;
			}
			else
			{
				int b = 0;
			}

			pDigits[i] = tempPointer;

			if( !counted[ tempPointer ] )
			{
				counted[ tempPointer ] = true;
				++CountedNumbers;
			}
		}
		if(false == changed)	return 0;
		++k;
		//cout << k;

	}
	return k*iNumber;

}

int main()
{
	//Read numbers
	list<int> numbers;
	int count = 0;
	ReadCases( numbers,count );
	
	//Count numbers
	int index = 1;
	for (list<int>::iterator it = numbers.begin(); it != numbers.end(); ++it)
	{
		 int result = CountNumbers(*it);
		 Output(index, result);
		 ++index;
	}

	return 0;
}