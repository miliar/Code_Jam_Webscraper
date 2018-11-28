#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

//auto& in  = std::cin;
//auto& out = std::cout;

const char MINUS_ONE = '-';
const char ONE = '1';

char table[128][128];
char mul(char a, char b) {
	return table[a][b];
}

int main() {
	std::ifstream in("C-small-attempt8.in");
	std::ofstream out("output.txt");

	table[ONE][ONE] = ONE;
	table[ONE]['i'] = 'i';
	table[ONE]['j'] = 'j';
	table[ONE]['k'] = 'k';
	table[ONE][MINUS_ONE] = MINUS_ONE;
	table[ONE]['I'] = 'I';
	table[ONE]['J'] = 'J';
	table[ONE]['K'] = 'K';

	table['i'][ONE] = 'i';
	table['i']['i'] = MINUS_ONE;
	table['i']['j'] = 'k';
	table['i']['k'] = 'J';
	table['i'][MINUS_ONE] = 'I';
	table['i']['I'] = ONE;
	table['i']['J'] = 'K';
	table['i']['K'] = 'j';

	table['j'][ONE] = 'j';
	table['j']['i'] = 'K';
	table['j']['j'] = MINUS_ONE;
	table['j']['k'] = 'i';
	table['j'][MINUS_ONE] = 'J';
	table['j']['I'] = 'k';
	table['j']['J'] = ONE;
	table['j']['K'] = 'I';

	table['k'][ONE] = 'k';
	table['k']['i'] = 'j';
	table['k']['j'] = 'I';
	table['k']['k'] = MINUS_ONE;
	table['k'][MINUS_ONE] = 'K';
	table['k']['I'] = 'J';
	table['k']['J'] = 'i';
	table['k']['K'] = ONE;

	table[MINUS_ONE][ONE] = MINUS_ONE;
	table[MINUS_ONE]['i'] = 'I';
	table[MINUS_ONE]['j'] = 'J';
	table[MINUS_ONE]['k'] = 'K';
	table[MINUS_ONE][MINUS_ONE] = ONE;
	table[MINUS_ONE]['I'] = 'i';
	table[MINUS_ONE]['J'] = 'j';
	table[MINUS_ONE]['K'] = 'k';

	table['I'][ONE] = 'I';
	table['I']['i'] = ONE;
	table['I']['j'] = 'K';
	table['I']['k'] = 'j';
	table['I'][MINUS_ONE] = 'i';
	table['I']['I'] = MINUS_ONE;
	table['I']['J'] = 'k';
	table['I']['K'] = 'J';

	table['J'][ONE] = 'J';
	table['J']['i'] = 'k';
	table['J']['j'] = ONE;
	table['J']['k'] = 'I';
	table['J'][MINUS_ONE] = 'j';
	table['J']['I'] = 'K';
	table['J']['J'] = MINUS_ONE;
	table['J']['K'] = 'i';

	table['K'][ONE] = 'K';
	table['K']['i'] = 'J';
	table['K']['j'] = 'i';
	table['K']['k'] = ONE;
	table['K'][MINUS_ONE] = 'k';
	table['K']['I'] = 'j';
	table['K']['J'] = 'I';
	table['K']['K'] = MINUS_ONE;

	int t; in >> t;
	for (int k = 1; k <= t; ++k) {
		int l, x; in >> l >> x;
		std::string str; in >> str;

		std::string tmp = str;
		str = "";
		for (int i = 0; i < x; ++i)
			str += tmp;

		std::vector<int> is;
		std::vector<char> products;

		char product = ONE;
		for (int i = 0; i < l*x; ++i) {
			product = mul(product, str[i]);
			if (product == 'i') {
				is.push_back(i);
			}
			products.push_back(product);
		}

		std::string result = "NO";

		if (product == MINUS_ONE) {
			product = ONE;
			for (int i = l*x - 1; i >= 1; --i) {
				product = mul(str[i], product);

				if (product == 'k'
					&& products[i-1] == 'k'
					&& std::find_if(is.begin(), is.end(),
						[&](int m) { return m < i-1; }) != is.end())
				{
					result = "YES";
					break;
				}
			}
		}

		out << "Case #" << k << ": " << result << '\n';
	}

	return 0;
}