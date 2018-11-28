#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

bool & is_Palindrome(double &rInputNumber)
{
	string palindromeScanner;
	int stringLength;
	bool isPalindrome=true;
	bool &rIsPalindrome=isPalindrome;
	double stringCenter;

	//convert number to string
	palindromeScanner=to_string((long double)rInputNumber);

	//get length of string
	stringLength=palindromeScanner.length();

	//get string center char
	stringCenter=((double)stringLength-1)/2;

	//test for palindrometrical symetry
	for (double centerDisplacement=stringCenter; centerDisplacement>0; centerDisplacement--)
	{

		//see if chars 'centerDisplacement' length from the center of the string are equal
		if (palindromeScanner[stringCenter+centerDisplacement]!=palindromeScanner[stringCenter-centerDisplacement])
			isPalindrome=false;

		//isPalindrome=false if not symetrical
	}

	//return bool indicator of palindrometrical symetry, denoted by isPalindrome
	return rIsPalindrome;
}

int main()
{
	//variable declarations
	int numberOfCases, numberOfPalindromes=0;
	int &rNumberOfCases=numberOfCases;
	double bounds[2], scanningCounterSquare;
	double &rL_Bounds=bounds[0];
	double &rU_Bounds=bounds[1];
	int scanningBounds[2];
	string uselessString;


	//open files

	string inDocName, outDocName;

	cout<<"Input Document Name: ";
	cin>>inDocName;

	//getOutputName
	cout<<"Output Document Name: ";
	cin>>outDocName;
	
	//skip line
	cout<<endl;

	//open files

	ifstream inDoc(inDocName);
	ofstream outDoc(outDocName);

	//test to see if documents are open
	if (!inDoc.is_open())
	{
		cerr<<"Document Names are Invalid"<<endl;

		//wait for user response
		cin>>uselessString;

		//close documents
		inDoc.close();
		outDoc.close();

		return 1;
	}


	//start first line of output
	outDoc<<"Case #1: ";




	//get number of cases
	inDoc>>numberOfCases;

	//start case processing loop(main loop)

	for (int caseCounter=1; caseCounter<=numberOfCases; caseCounter++)
	{

		//get bounds
		inDoc>>rL_Bounds;
		inDoc>>rU_Bounds;

		//set scanning bounds
		scanningBounds[0]=ceil(sqrt(bounds[0]));
		scanningBounds[1]=floor(sqrt(bounds[1]));

		//start scan from lower to upper bounds
		for (double scanningCounter=scanningBounds[0]; scanningCounter<=scanningBounds[1]; scanningCounter++)
		{
			
			//check for palindrome
			if (is_Palindrome((double&)scanningCounter))
			{
				//if is a palindrome, check if square is a palindrome

				//get square of counter
				scanningCounterSquare=pow(scanningCounter,2);

				//if square is a palindrome, incrament the number of palindromes we have found
				if (is_Palindrome((double&)scanningCounterSquare))
					numberOfPalindromes++;
			}

			//otherwise we start scanning the next integer.
		}
		
		//now we output the number of palindromes we have found
		outDoc<<numberOfPalindromes;

		if (caseCounter!=numberOfCases)
		{
			//make reference to caseCounter
			int caseCounterTemp=caseCounter+1;
			int &rCaseCounterTemp=caseCounterTemp;
			outDoc<<endl<<"Case #"<<rCaseCounterTemp<<": ";
		}

		//reset the number of palindromes
		numberOfPalindromes=0;
	}
	//tell the user we're done
	cout<<"Done"<<endl;

	//wait for response before closing
	cin>>uselessString;

	//close mainStream
	inDoc.close();
	outDoc.close();

	return 0;
}