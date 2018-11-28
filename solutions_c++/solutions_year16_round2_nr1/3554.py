#include <fstream>
#include <vector>
#include <string>
#include <iostream>

void solve_case()
{
	std::string str;
	std::cin >> str;
	
	std::vector< int > letters('Z' - 'A', 0);
	for(std::string::const_iterator it = str.begin(); it < str.end(); ++it)
	{
		++letters[*it - 'A'];
	}
	
	const int z = letters['Z' - 'A'];
	const std::string zeros(z, '0');
	letters['Z' - 'A'] -= z;
	letters['E' - 'A'] -= z;
	letters['R' - 'A'] -= z;
	letters['O' - 'A'] -= z;

	const int w = letters['W' - 'A'];
	const std::string twos(w, '2');
	letters['T' - 'A'] -= w;
	letters['W' - 'A'] -= w;
	letters['O' - 'A'] -= w;

	const int x = letters['X' - 'A'];
	const std::string sixs(x, '6');
	letters['S' - 'A'] -= x;
	letters['I' - 'A'] -= x;
	letters['X' - 'A'] -= x;

	const int s = letters['S' - 'A'];
	const std::string sevens(s, '7');
	letters['S' - 'A'] -= s;
	letters['E' - 'A'] -= s;
	letters['V' - 'A'] -= s;
	letters['E' - 'A'] -= s;
	letters['N' - 'A'] -= s;

	const int u = letters['U' - 'A'];
	const std::string fours(u, '4');
	letters['F' - 'A'] -= u;
	letters['O' - 'A'] -= u;
	letters['U' - 'A'] -= u;
	letters['R' - 'A'] -= u;

	const int r = letters['R' - 'A'];
	const std::string threes(r, '3');
	letters['T' - 'A'] -= r;
	letters['H' - 'A'] -= r;
	letters['R' - 'A'] -= r;
	letters['E' - 'A'] -= r;
	letters['E' - 'A'] -= r;

	const int o = letters['O' - 'A'];
	const std::string ones(o, '1');
	letters['O' - 'A'] -= o;
	letters['N' - 'A'] -= o;
	letters['E' - 'A'] -= o;

	const int f = letters['F' - 'A'];
	const std::string fives(f, '5');
	letters['F' - 'A'] -= f;
	letters['I' - 'A'] -= f;
	letters['V' - 'A'] -= f;
	letters['E' - 'A'] -= f;

	const int g = letters['G' - 'A'];
	const std::string eights(g, '8');
	letters['E' - 'A'] -= g;
	letters['I' - 'A'] -= g;
	letters['G' - 'A'] -= g;
	letters['H' - 'A'] -= g;
	letters['T' - 'A'] -= g;

	const int i = letters['I' - 'A'];
	const std::string nines(i, '9');
	letters['N' - 'A'] -= i;
	letters['I' - 'A'] -= i;
	letters['N' - 'A'] -= i;
	letters['E' - 'A'] -= i;

	std::cout << zeros << ones << twos << threes << fours << fives << sixs << sevens << eights << nines;
	//std::cout << letters['O'-'A'];
	return;
}

int main(int argc, char* argv[])
{
	unsigned T;
	
	//freopen ("A.in", "r", stdin);		//input file
	//freopen ("A.out", "w", stdout);		//output file
	std::cin >> T;
	for( int i = 0; i < T; ++i )
	{
		std::cout << "Case #" << i+1 << ": ";
		solve_case();
		std::cout << std::endl;
		
	}
	
	return 0;
}