// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <math.h>

bool isFair( int inNumber ){
	int BeforeNumber = inNumber;
	std::stringstream ss;
	ss << inNumber;
	std::string aNumberString = ss.str();
	std::reverse( aNumberString.begin(), aNumberString.end() ); 

	int AfterNumber = atoi( aNumberString.c_str() );
	if ( BeforeNumber == AfterNumber )
		return true;
	return false;
}

int getSquareRoot( double inNumber ){
	double aSquareRoot = sqrt( inNumber );
	// Check if decimal place.
	if ( ( aSquareRoot / (int)aSquareRoot ) != 1 )
		return 0;
	return aSquareRoot;
}

int getNumberOfFairAndSquare( int before, int after ){
	return 1;
}

std::string outputResultFromLine( std::string inLine ){
	std::string aLine = inLine;
	int firstInt = atoi( inLine.substr( 0, inLine.find( " " ) ).c_str() );
	aLine = aLine.substr( aLine.find( " " ) + 1 );
	int secondInt = atoi( aLine.c_str() );
	int count = 0;
	for ( int i = firstInt; i <= secondInt; i++ ){
		if ( isFair( i ) == true ) {
			int Squared = getSquareRoot( i );
			if ( Squared == 0 )
				continue;
			if ( isFair( Squared ) == true ) {
				count = count + 1;
				continue;
			}
		}
	}
	return std::to_string((long double)count);
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::cout << "Starting of File." << std::endl;
	std::string aLine;

	std::ofstream outputFile;
	outputFile.open( "FairAndSquareOutput.txt" );

	std::ifstream myfile("C-small-attempt0.in");
	bool readFirst = false;
	int i = 1;
	if ( myfile.is_open() ){
		while( myfile.good() ){
			getline(myfile, aLine);
			if ( readFirst == false ) {
				std::cout << "First line is " << aLine << std::endl;
				readFirst = true;
				continue;
			}
			std::cout << "This line is " << aLine << std::endl;
			std::string ToPrint = "Case #" + std::to_string((long double)i) + ": " + outputResultFromLine( aLine );
			std::cout << "ToPrint is " << ToPrint << std::endl;
			outputFile << ToPrint << std::endl;
			i = i + 1;
		}
	}

	outputFile.close();

	std::string EndString;
	std::cin >> EndString;

	return 0;
}

