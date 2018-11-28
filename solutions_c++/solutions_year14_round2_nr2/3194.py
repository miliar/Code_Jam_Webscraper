// CodeJam.cpp : Defines the entry point for the console application.
//
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

//char const * Feglawon = "Fegla Won";
size_t Calculate(size_t A, size_t B, size_t K)
{
	size_t counter = 0;
	size_t Aval = std::min(A, B);
	size_t Bval = std::max(A, B);
	if( K <= Bval && K <=Aval )
	{
	
	counter = Bval * K;
	for( size_t i = K; i < Aval; i++ )
	{

		for( size_t j = 0; j < Bval; j++ )
		{
			if( ( i & j ) < K )
				counter++;
		}

	}
	}
else
{
	for( size_t i = 0; i < Aval; i++ )
	{

		for( size_t j = 0; j < Bval; j++ )
		{
			if( ( i & j ) < K )
				counter++;
		}

	}
}
	return counter;
}

ofstream output("D:\\out_1B_2.txt");



int main()
{
	ifstream file;
	file.open("D:\\in_1B_2.in");
	int counter;
	char in[20];
	file >> in;
	counter = atoi(in);

	int testnum = 1;
	while( !file.eof() )
	{
		file >> in;
		size_t A = atoi(in);
		file >> in;
		size_t B = atoi(in);
		file >> in;
		size_t K = atoi(in);
		
		
		size_t winner = Calculate(A,B,K);
		output << "Case #" << testnum << ": " << winner << endl;
				cout << "Case #" << testnum << ": " << winner << endl;
			
		testnum++;
		if( testnum == counter +1 )
			break;
		
	}
	file.close();
	output.close();
	return 0;
}

