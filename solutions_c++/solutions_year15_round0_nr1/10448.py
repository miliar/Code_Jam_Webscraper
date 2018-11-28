#include <fstream>
#include <iostream>
#include <sstream>

int main( int argc, char *argv[] )
{
	std::ifstream is("A-small-attempt0.in");
	std::string line;
	std::getline( is, line );
	std::istringstream ss(line);
	int T = 0;

	ss >> T;

	int n;
	char c;
	int shy;
	for(int t = 1; t <= T; ++t)
	{
		std::getline( is, line );
		std::istringstream ss(line);
		ss >> n;

		int standing = 0;
		int invite = 0;
		for(int i = 0; i < n+1; ++i)
		{
			ss >> c;
			shy = c - 48;

			if ( shy == 0 && standing <= i )
			{
				standing++;
				invite++;
			}
			else
			{
				standing += shy;
			}
		}

		std::cout << "Case #" << t << ": " << invite << std::endl;
	}

	return 0;
}
