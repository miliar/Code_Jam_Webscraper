//Fair and Square

#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <functional>
#include <cmath>

using namespace std;

bool palindrome(unsigned long);
unsigned long nextPerfectSquare(unsigned long, double[]);

int main(){

	string filename;
	ifstream inputFile;
	ofstream outputFile;
	int lowEnd, highEnd;

	cout << "Please enter the name of the input file with extension\n" ;
	cin >> filename;

	inputFile.open(filename.c_str());
	outputFile.open("output2.txt");

	unsigned long numCases=0, counter=0;
	double perfectSquares[10000];

	for (unsigned long num=0; num < 10000; num++){
		perfectSquares[num] = pow(num,2);
	}

	inputFile >> numCases;

	for (unsigned long j=1; j<=numCases; j++){
		inputFile >> lowEnd;
		inputFile >> highEnd;
		counter = 0;
		unsigned long i = lowEnd;

		while (i <= highEnd){
			float root = sqrt(i);
			if ((root - (unsigned long)root) == 0){
				if (palindrome(i) && palindrome((unsigned long)root))
					counter++;
			}
			i = nextPerfectSquare(i, perfectSquares);
		}
		
		outputFile << "Case #" << j << ": " << counter << endl;
	}
	
}

bool palindrome(unsigned long n){
  unsigned long x = n;
  unsigned long u = 0;
  while (x)
    {
	    u *= 10;
	    u += x % 10;
	    x /= 10;
    }
  return (n == u);
}

unsigned long nextPerfectSquare(unsigned long num, double array[10000]){
	unsigned long result;

	unsigned long position = (unsigned long)(sqrt(num));
	result = (unsigned long)(array[position+1]);

	return result;
}