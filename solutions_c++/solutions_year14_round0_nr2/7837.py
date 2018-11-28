#define _CRT_SECURE_NO_WARNINGS
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
	readFile("D:/C++/Competitions/Codejam 2014/Magick trick/B-large.in", in);

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
			for(unsigned N=0;lIT!=lines.end();++lIT, ++N)
			{
				boost::tokenizer<boost::char_separator<char>> tokens(*lIT, boost::char_separator<char>(" \t"));
				auto tIT=tokens.begin();
				if(tIT!=tokens.end())
				{
					double C=atof(tIT->c_str());
					if(++tIT!=tokens.end())
					{
						double F=atof(tIT->c_str());
						if(++tIT!=tokens.end())
						{
							double X=atof(tIT->c_str());
							double t=X/2;

							char LOL_buf[100];
							LOL_out<<"Case #"<<N+1<<": ";
							for(unsigned n=0;;++n)
							{
								double change=C/(2+n*F)+X*(1/(2+(n+1)*F)-1/(2+n*F));
								if(change>0)
								{
									sprintf(LOL_buf, "%.7f", t);
									LOL_out<<LOL_buf<<'\n';
									break;
								}
								t+=change;
							}
						}
					}
				}
			}
		}
	}
	std::ofstream out_thing("D:/C++/Competitions/Codejam 2014/Magick trick/out3.txt");
	out_thing<<LOL_out.str();
	out_thing.close();
}