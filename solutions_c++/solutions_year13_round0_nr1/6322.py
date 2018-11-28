#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

int main()
{
	int t;
	{
		std::string s;
		std::getline(std::cin, s);
		std::istringstream ss(s);
		ss >> t;
	}

	for (int i = 0; i < t; ++i)
	{
		char m[4][4];
		for (int i = 0; i < 4; ++i)
		{
			std::string s;
			std::getline(std::cin, s);
			std::copy_n(s.begin(), 4, m[i]);
		}

		bool
			x = false,
			o = false,
			c = std::find(&m[0][0], &m[3][3], '.') == &m[3][3]; // game completed

		bool
			xxxx = true, xxxxx = true,
			oooo = true, ooooo = true;
			
		for (int i = 0; i < 4; ++i)
		{
			bool
				xx = true, xxx=true,
				oo = true, ooo=true;

			for (int j = 0; j < 4; ++j)
			{
				switch (m[i][j])
				{
					case 'X': oo = false; break;
					case 'O': xx = false; break;
					case '.':
					xx = false;
					oo = false;
				}

				switch (m[j][i])
				{
					case 'X': ooo = false; break;
					case 'O': xxx = false; break;
					case '.':
					xxx = false;
					ooo = false;
				}
			}

			x |= xx || xxx;
			o |= oo || ooo;
			
			switch (m[i][i])
			{
				case 'X': oooo = false; break;
				case 'O': xxxx = false; break;
				case '.':
				xxxx = false;
				oooo = false;
			}
			
			switch (m[i][3-i])
			{
				case 'X': ooooo = false; break;
				case 'O': xxxxx = false; break;
				case '.':
				xxxxx = false;
				ooooo = false;
			}
		}
		
		x |= xxxx || xxxxx;
		o |= oooo || ooooo;

		std::cout << "Case #" << i + 1 << ": " <<
			(x ? (o ? "Draw" : "X won") : (o ? "O won" : (c ? "Draw" : "Game has not completed"))) <<
			std::endl;

		std::string s;
		std::getline(std::cin, s);
	}
}
