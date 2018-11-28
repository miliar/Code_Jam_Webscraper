//============================================================================
// Name        : task1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>

int main()
{
	std::fstream f;
	f.open("A-large.in");

	int T = 0;
	f >> T;

	for (int i = 0; i < T; ++i)
	{
		std::string word;
		f >> word;

		std::string out;
		out += word[0];
		for (int n = 1; n < word.size(); ++n)
		{
			if (word[n] >= out[0])
			{
				out = word[n] + out;
			}
			else
			{
				out = out + word[n];
			}
		}

		std::cout << "Case #" << (i+1) << ": " << out << std::endl;
	}
}












