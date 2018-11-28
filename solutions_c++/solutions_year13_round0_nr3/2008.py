#include <Windows.h>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

std::string ReadString;
std::ofstream OutputFile;
std::ifstream InputFile;
std::stringstream StringStream;

const unsigned long long int MIN_NUMBER = 1;
const unsigned long long int MAX_NUMBER = 100000000000000;

unsigned long long int * FairAndSquareArray;
int nsizeOfFairAndSquareArray;

bool IsPalindrom( std::string palinNum );
int numOfFS( unsigned long long int floor, unsigned long long int ceil );

int main() {
	// Finds all accetable numbers
	FairAndSquareArray = new unsigned long long int[250];
	unsigned long long int numToSquare = 0;
	unsigned long long int squarednum = 0;
	while( squarednum <= MAX_NUMBER ) {
		std::string palinNum;
		//Check if it is a plaindrome
		StringStream.clear();
		StringStream.str("");
		StringStream << numToSquare;
		StringStream >> palinNum;

		if( IsPalindrom(palinNum) ) {
			//Check if it is a plaindrome
			squarednum = numToSquare * numToSquare;
			StringStream.clear();
			StringStream.str("");
			StringStream << squarednum;

			StringStream >> palinNum;

			if( IsPalindrom(palinNum) ) {
				FairAndSquareArray[nsizeOfFairAndSquareArray] = squarednum;
				nsizeOfFairAndSquareArray++;
				std::cout << squarednum << "\n" << MAX_NUMBER << "\n";
			}
		}
		numToSquare++;
		squarednum = numToSquare * numToSquare;
	}

	//Opens the file and creates an input file
	OutputFile = std::ofstream("outputLarge.out");

	while( !InputFile.is_open() ) {
		std::cout << "Enter input File Name:\n";
		std::string fileName;
		std::cin >> fileName;
		InputFile = std::ifstream( fileName );
		//InputFile = std::ifstream( "C-small-attempt0.in" );
		//InputFile = std::ifstream( "input.in" );
	};

	getline( InputFile, ReadString );
	StringStream.clear();
	StringStream.str( ReadString );
	int numOfCases;
	StringStream >> numOfCases;
	std::cout << numOfCases << "\n";
	
	//Checks for the numbers
	for( int i = 0; i < numOfCases; i++ ) {
		getline( InputFile, ReadString );
		StringStream.clear();
		StringStream.str( ReadString );

		unsigned long long int floor;
		unsigned long long int ceil;
		StringStream >> floor;
		StringStream >> ceil;

		OutputFile << "Case #" << (i+1) << ": " << numOfFS(floor, ceil);
		if( i < numOfCases-1 ) { OutputFile << "\n"; }
	}
	
	OutputFile.close();
	InputFile.close();

	//while( true ) {}
	return 0;
}


bool IsPalindrom( std::string palinNum ) {
	bool isPalindrome = true;
	int head = 0, tail = palinNum.size()-1;
	while( head <= tail ) {
		if( palinNum[head] != palinNum[tail] ) {isPalindrome = false; }
		head++;
		tail--;
	}

	return isPalindrome;
}

int numOfFS( unsigned long long int floor, unsigned long long int ceil ) {
	int numToReturn = 0;

	for( int i = 0; i < nsizeOfFairAndSquareArray; i++ ) {
		if( floor <= FairAndSquareArray[i] && ceil >= FairAndSquareArray[i] ) {
			numToReturn++;
		}
	}

	return numToReturn;
}