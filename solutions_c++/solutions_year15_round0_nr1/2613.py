#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>

//#define small 
#define large

int main()
{
#if defined(small)
	std::ifstream in("A-small-attempt0.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#elif defined(large)
	std::ifstream in("A-large.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif
	short T;
	std::cin >> T;
	short SMax;
	std::string s;
	for (short i = 1; i <= T; i++){
		std::vector<int> Si;
		std::cin >> SMax;
		std::cin >> s;
		for (short j = 0; j <= SMax; j++)
			Si.push_back(s[j] - '0');

		int friends = 0, standing = 0;
		for (short j = 0; j <= SMax; j++){
			standing = standing + Si[j];
			if (j < SMax & j+1 > standing){
				standing = standing++;
				friends = friends++;
			}
		}

		std::cout << "Case #" << i << ": " << friends << std::endl;
	}
}