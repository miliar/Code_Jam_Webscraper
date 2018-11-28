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
	std::string const file_name ("D:/Downloads/D-large");
	std::ifstream inFile (file_name+".in");
	if (!inFile.is_open())
		return 0;

	std::ofstream outFile (file_name+".out");
	if (!outFile.is_open())
		return 0;

	int const T = getline<int> (inFile); // number of test cases

	// Iterate cases
	for ( int n = 0; n < T; n++ )
	{
		typedef std::vector<double> blocks;
		auto init_blocks = [&](size_t N){
			blocks blocks (0);
			blocks.reserve(N);
			for ( size_t i = 0; i < N; ++i )
				blocks.push_back (getline<double>(inFile));
			std::sort(blocks.begin(),blocks.end());
			return blocks;
		};

		// Inputs
		auto const N = getline<int> (inFile); // number of blocks
		auto Naomi_blocks = init_blocks(N); // Naomi's blocks,
		auto Ken_blocks = init_blocks(N); // Ken's blocks
		
		// Initial scores
		size_t const Naomi_Deceitful_scores = [](blocks Naomi_blocks, blocks Ken_blocks){
			size_t Naomi_Deceitful_scores = 0;
			while(!Naomi_blocks.empty())
			{
				bool Naomi_sign = Naomi_blocks.back() > Ken_blocks.back();

				Naomi_Deceitful_scores += 1 * Naomi_sign;

				Ken_blocks.pop_back();
				//Naomi_blocks.erase(Naomi_blocks.begin());
				if ( Naomi_sign )
					Naomi_blocks.pop_back();
				else
					Naomi_blocks.erase(Naomi_blocks.begin());
			}
			return Naomi_Deceitful_scores;
		}(Naomi_blocks, Ken_blocks);

		size_t const Naomi_War_scores = [](blocks Naomi_blocks, blocks Ken_blocks){
			size_t Naomi_War_scores = 0;
			while(!Naomi_blocks.empty())
			{
				bool Naomi_sign = Naomi_blocks.back() > Ken_blocks.back();

				Naomi_War_scores += 1 * Naomi_sign;

				Naomi_blocks.pop_back();
				if ( Naomi_sign )
					Ken_blocks.erase(Ken_blocks.begin());
				else
					Ken_blocks.pop_back();
			}
			return Naomi_War_scores;
		}(Naomi_blocks, Ken_blocks);


		// print result
		outFile << "Case #" << n+1 << ": ";
		outFile << Naomi_Deceitful_scores << ' ' << Naomi_War_scores;
		outFile << '\n';
	}
		
	inFile.close();
	outFile.close();


	return 0;
}

