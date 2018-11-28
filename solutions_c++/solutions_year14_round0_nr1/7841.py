#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<list>
#include<string>
#include<sstream>
#include<iostream>
#include<fstream>
#include<boost/tokenizer.hpp>
void readFile(char const* file, std::string &str)
{
	FILE *f;
	fopen_s(&f, file, "r");
	if(f)
	{
		std::fseek(f, 0, SEEK_END);
		str.resize(std::ftell(f));
		std::rewind(f);
		std::fread(&*str.begin(), 1, str.size(), f);
		std::fclose(f);
	}
	else throw std::system_error(std::error_code(), "Can't open file");
}
struct Trick
{
	int ans1, cards1[4][4], ans2, cards2[4][4], nGuesses, guess;
};
void main()
{
	std::string in;
	readFile("D:/C++/Competitions/Codejam 2014/Magick trick/A-small-attempt1.in", in);

	unsigned nTricks;
	std::stringstream LOL_out;
	{
		boost::tokenizer<boost::char_separator<char>> lines(in, boost::char_separator<char>("\r\n"));
		auto lIT=lines.begin();
		if(lIT!=lines.end())
		{
		//	nTricks=std::atoi(lIT->c_str());
			++lIT;

			auto &LOL=lines.end();
			for(unsigned N=0;lIT!=lines.end();++N)
			{
				Trick trick;
				trick.ans1=std::atoi(lIT->c_str())-1;
				if(++lIT!=lines.end())
				{
					for(unsigned k=0;k<4&&lIT!=lines.end();++k, ++lIT)
					{
						unsigned k2=0;
						for(auto &token:boost::tokenizer<boost::char_separator<char>>(*lIT, boost::char_separator<char>(" \t")))
							trick.cards1[k][k2++]=std::atoi(token.c_str());
					}
				}
				trick.ans2=std::atoi(lIT->c_str())-1;
				if(++lIT!=lines.end())
				{
					for(unsigned k=0;k<4&&lIT!=lines.end();++k, ++lIT)
					{
						unsigned k2=0;
						for(auto &token:boost::tokenizer<boost::char_separator<char>>(*lIT, boost::char_separator<char>(" \t")))
							trick.cards2[k][k2++]=std::atoi(token.c_str());
					}
				}

				//
				trick.nGuesses=0;
				for(unsigned k=0;k<4;++k)
				{
					for(unsigned k2=0;k2<4;++k2)
						if(trick.cards1[trick.ans1][k]==trick.cards2[trick.ans2][k2])
							trick.guess=trick.cards1[trick.ans1][k], ++trick.nGuesses;
				}
				LOL_out<<"Case #"<<N+1<<": ";
				switch(trick.nGuesses)
				{
				case 0:LOL_out<<"Volunteer cheated!\n";break;
				case 1:LOL_out<<trick.guess<<"\n";break;
				default:LOL_out<<"Bad magician!\n";break;
				}
				//

				if(lIT==lines.end())
					break;
			}
		}
	}
	std::ofstream out_thing("D:/C++/Competitions/Codejam 2014/Magick trick/out");
	out_thing<<LOL_out.str();
	out_thing.close();
}