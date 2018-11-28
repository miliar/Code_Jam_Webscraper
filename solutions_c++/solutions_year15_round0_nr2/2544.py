#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

#define small
//#define large

short find_optimum(std::vector<short> &Pi, int eat_min){
	if (Pi.size() == 0)
		return eat_min;
	short n, optimum;
	float D;
	D = Pi[0], n = 0;
	for (short j = 0; (Pi.size() > j) & n == j; j++)
		if (Pi[j] == D)
			n++;
	std::vector<short> Pi_rest(Pi.begin() + n, Pi.end());
	optimum = 2 ^ 15 - 1;
	for (float k = 1; k <= D; k++){
		int specials_this = (k - 1)*n;
		int eat_this = std::max(static_cast<int> (ceil(D / k)), eat_min);
		int eat_total_plus_specials_other = find_optimum(Pi_rest, eat_this);
		int total = specials_this + eat_total_plus_specials_other;
		if (total < optimum)
			optimum = total;
	}
	return optimum;
}

int main()
{
#if defined(small)
	std::ifstream in("B.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#elif defined(large)
	std::ifstream in("B-large.in");
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
	std::ofstream out("out.out");
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

	short T, D, y;
	char c;
	std::cin >> T;
	for (short i = 1; i <= T; i++){
		std::vector<short> Pi;
		std::cin >> D;
		for (short j = 1; j <= D; j++){
			std::cin >> c;
			Pi.push_back(c - '0');
		}
		std::sort(Pi.begin(), Pi.end(), std::greater<short>());
		y = find_optimum(Pi, 0);

		std::cout << "Case #" << i << ": " << y << std::endl;
	}
}