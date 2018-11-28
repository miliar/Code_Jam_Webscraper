#include <iostream>
#include <fstream>

using namespace std;

//this ought to be more than enough room for the intended size
char palindromeScratchSpace[32];

inline bool isPalindrome(unsigned long numberToCheck)
{
	int numDigits=0;
	bool bIsPalindrome=true;

	//start peeling off digits
	while (numberToCheck > 0)
	{
		palindromeScratchSpace[numDigits]=numberToCheck%10;
		numberToCheck=(numberToCheck-palindromeScratchSpace[numDigits])/10;
		numDigits++;
	}

	//simplifies later logic
	if (numDigits>0)
	{
		numDigits--;
	}

	//actually perform the palindrome check
	for (int i=0; (i<numDigits) && bIsPalindrome; ++i)
	{
		if (palindromeScratchSpace[i]!=palindromeScratchSpace[numDigits-i])
		{
			bIsPalindrome=false;
		}
	}

	return bIsPalindrome;
}

//a freaky and fast sqrt function for unsigned longs
inline unsigned long uiSqrt(unsigned long x)
{
    unsigned long c = 0x80000000;
    unsigned long g = 0x80000000;

    while(1) {
        if(g*g > x)
            g ^= c;
        c >>= 1;
        if(c == 0)
            return g;
        g |= c;
    }

    return 0;
}

int main()
{
	ifstream input_file("C-small-attempt0.in");
	ofstream output_file("C-small-attempt0.out");
	unsigned long limitA, limitB;
	unsigned long limitASqrt, limitBSqrt;
	unsigned long iter;
	unsigned long numFairAndSquare;

	int numTestCases;

	//get the number of test cases
	input_file >> numTestCases;
	input_file.get();

	cout << "There are " << numTestCases << " test cases." << endl;

	//iterate over the test cases
	for (int t = 0; t<numTestCases; ++t)
	{
		//reset
		numFairAndSquare=0;

		//perform calculations - this will work on the small, maybe the first large, but not the second large...
		input_file >> limitA >> limitB;
		input_file.get();
		limitASqrt = uiSqrt(limitA);
		limitBSqrt = uiSqrt(limitB);
		for (unsigned long sqrtIter=limitASqrt; sqrtIter<=limitBSqrt; ++sqrtIter)
		{
			iter=sqrtIter*sqrtIter;
			if ((iter>=limitA) && (iter<=limitB))
			{
				if (isPalindrome(sqrtIter))
				{
					if (isPalindrome(iter))
					{
						numFairAndSquare++;
					}
				}
			}
		}

		output_file << "Case #" << t +1 << ": " << numFairAndSquare << endl;
	}

	input_file.close();
	output_file.close();

	return 0;
}
