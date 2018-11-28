#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

#define small 
//#define large

int main()
{
#if defined(small)
	std::ifstream in("D-small-attempt3.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#elif defined(large)
	std::ifstream in("D-large.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

	short T;
	std::cin >> T;
	for (short i = 1; i <= T; i++){
		short X, R, C;
		std::string winner = "GABRIEL";
		std::cin >> X;
		std::cin >> R;
		std::cin >> C;
		if (floor((X + 1) / 2) > std::min(R, C))
			winner = "RICHARD";
		if (X > std::max(R, C))
			winner = "RICHARD";
		if (R*C%X != 0)
			winner = "RICHARD";
		if (std::min(R, C) == 2 & X >= 4 & R*C <= 2*X)
			winner = "RICHARD";
		if (std::min(R, C) == 3 & X >= 6 & R*C <= 2*X)
			winner = "RICHARD";
		if (X > 7)
			winner = "RICHARD";
		std::cout << "Case #" << i << ": " << winner << std::endl;
	}
}