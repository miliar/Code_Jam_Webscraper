#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <cassert>


std::string solve(std::string &s)
{
	std::map<char, int> mapc;
	std::map<int, int>  mapd;
	for (auto& c: s)
		mapc[c]++;
	// ZERO
	int zero = mapc['Z'];
	mapd[0] = zero;
	mapc['Z'] -= zero;
	mapc['E'] -= zero;
	mapc['R'] -= zero;
	mapc['O'] -= zero;
	// EIGHT
	int eight = mapc['G'];
	mapd[8] = eight;
	mapc['E'] -= eight;
	mapc['I'] -= eight;
	mapc['G'] -= eight;
	mapc['H'] -= eight;
	mapc['T'] -= eight;
	// THREE
	int three = mapc['H'];
	mapd[3] = three;
	mapc['T'] -= three;
	mapc['H'] -= three;
	mapc['R'] -= three;
	mapc['E'] -= three * 2;
	assert(!mapc['H']);
	// FOUR
	int four = mapc['R'];
	mapd[4] = four;
	mapc['F'] -= four;
	mapc['O'] -= four;
	mapc['U'] -= four;
	mapc['R'] -= four;
	assert(!mapc['U']);
	// FIVE
	int five = mapc['F'];
	mapd[5] = five;
	mapc['F'] -= five;
	mapc['I'] -= five;
	mapc['V'] -= five;
	mapc['E'] -= five;
	// SEVEN
	int seven = mapc['V'];
	mapd[7] = seven;
	mapc['S'] -= seven;
	mapc['E'] -= seven * 2;
	mapc['V'] -= seven;
	mapc['N'] -= seven;
	// SIX
	int six = mapc['X'];
	mapd[6] = six;
	mapc['S'] -= six;
	mapc['I'] -= six;
	mapc['X'] -= six;
	assert(!mapc['S'] && !mapc['X']);
	// NINE
	int nine = mapc['I'];
	mapd[9] = nine;
	mapc['N'] -= nine * 2;
	mapc['I'] -= nine;
	mapc['E'] -= nine;
	// TWO
	int two = mapc['W'];
	assert(two == mapc['T']);
	mapd[2] = two;
	mapc['T'] -= two;
	mapc['W'] -= two;
	mapc['O'] -= two;
	// ONE
	int one = mapc['O'];
	assert(one == mapc['N'] && one == mapc['E']);
	mapd[1] = one;

	std::stringstream ss;
	for (auto& p: mapd)
		if (p.second)
			for (int i = 0; i < p.second; ++i)
				ss << p.first;
	return ss.str();
}

int main(int arc, char **argv)
{
	std::ifstream in;
	std::ofstream out;
	in. open(argv[1], std::ios_base::in);
	out.open(argv[2], std::ios_base::out);
	int T;

	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		std::string ss;
		in >> ss;
		out << "Case #" << i << ": " << solve(ss) << std::endl;
	}
	return 0;
}
