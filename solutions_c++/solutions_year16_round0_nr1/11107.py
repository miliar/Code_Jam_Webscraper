#include <stdio.h> // putchar()
#include <iostream>
#include <fstream> // input and out file streams

using namespace std; // Defined in line 31

long runTestCase( int N );

int main()
{
	int numTestCases;

	// Retrieving input values
	ifstream in("A-large.in",ios::in); //input file stream
	in >> numTestCases;

	int numbers[numTestCases];
	for(int i=0; i< numTestCases; i++){
		in >> numbers[i];
	}
	in.close(); //Close input file stream

	ofstream outputFile; // output file stream
	outputFile.open("output.txt");

	for(int i=0; i<numTestCases; i++){
		if( numbers[i] == 0 ){
			outputFile << "Case #" << i+1 << ": INSOMNIA\n";
		}else{
			long temp = runTestCase( numbers[i] ); //long is 8 bytes and should be enough. I could have used (long long), but it would take too much memory space (16bytes)
			outputFile << "Case #" << i+1 << ": " << temp << "\n";
		}
	}
	outputFile.close(); //close output file stream

	return 0;
}

long runTestCase( int N )
{
	bool numbersSeen[10];
	for(int i=0; i<10; i++){
		numbersSeen[i] = false;
	}
	bool done = false; //will determine when to stop
	long number, testNumber;
	for(int i=1; !done; i++) {
		number = i*N;
		testNumber = number;
		do {
			int digit = testNumber % 10;
			putchar('0' + digit);
			numbersSeen[digit] = true;
			testNumber /= 10;
		} while (testNumber > 0);
		bool testDone = true;
		for(int y=0; y<10; y++){
			if(numbersSeen[y] == false) { //If one number hasn't been seen yet, then break out of the for loop and continue counting
				testDone = false;
				break;
			}
		}
		done = testDone;
	}
	return number;
}
