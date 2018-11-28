#include "stdafx.h"

#include <array>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

template<typename T>
T getline ( std::ifstream& inFile ) {
	T line;
	inFile >> line;
	return line;
}

std::string getline<> ( std::ifstream& inFile ) {
	std::string line;
	getline (inFile, line);
	return line;
}


int main()
{
	std::string const file_name ("D:/Downloads/A-small-attempt0");
	std::ifstream inFile (file_name+".in");
	if (!inFile.is_open())
		return 0;

	std::ofstream outFile (file_name+".out");
	if (!outFile.is_open())
		return 0;

	int const T = getline<int> (inFile); // number of test cases
	std::string P; // prices of an item in the store

	std::cout << std::endl;

	// Iterate cases
	for ( int n = 0; n < T; n++ )
	{
		typedef std::vector<int const> card_arrangement;
		auto fill_arrangments = [&](){
			card_arrangement v(16);
			for ( size_t i = 0; i < 16; ++i )
				v[i] = getline<int> (inFile);
			return v;
		};

		auto const A1 = getline<int> (inFile); // answer to the first question
		auto AR1 = fill_arrangments ();
		auto const A2 = getline<int> (inFile); // answer to the second question
		auto AR2 = fill_arrangments ();
		
		auto AR1_st = AR1.begin() + (A1-1) * 4;
		auto AR1_end = AR1_st + 4;
		auto AR2_st = AR2.begin() + (A2-1) * 4;
		auto AR2_end = AR2_st + 4;
		std::sort (AR1_st, AR1_end);
		std::sort (AR2_st, AR2_end);

		card_arrangement res (4);
		auto it = std::set_intersection (
			AR1_st,
			AR1_end,
			AR2_st,
			AR2_end,
			res.begin() );

		auto const dist = std::distance ( res.begin(), it );
		
		// print result
		outFile << "Case #" << n+1 << ": ";
		if ( dist == 1 )
			outFile << res.front();
		else if ( dist == 0 )
			outFile << "Volunteer cheated!";
		else
			outFile << "Bad magician!";
		outFile << '\n';
	}
		
	inFile.close();
	outFile.close();


	return 0;
}

