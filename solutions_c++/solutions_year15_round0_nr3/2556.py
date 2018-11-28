#include <iostream>
#include <sstream>
#include <vector>

#define TABLE_WIDTH 8

const char MULTIPLICATION_TABLE[] = {
	0, 1, 2, 3, 4, 5, 6, 7,
	1, 4, 3, 6, 5, 0, 7, 2,
	2, 7, 4, 1, 6, 3, 0, 5,
	3, 2, 5, 4, 7, 6, 1, 0,
	4, 5, 6, 7, 0, 1, 2, 3,
	5, 0, 7, 2, 1, 4, 3, 6,
	6, 3, 0, 5, 2, 7, 4, 1,
	7, 6, 1, 0, 3, 2, 5, 4,
};

char DIVISION_TABLE_A[sizeof(MULTIPLICATION_TABLE)];  // f(c, b) = a
char DIVISION_TABLE_B[sizeof(MULTIPLICATION_TABLE)];  // f(c, a) = b

char I;
char J;
char K;
char JK;
char IJK;

static inline char
to_ord(char c)
{
	switch (c) {
	case '1': return 0;
	case 'i': return 1;
	case 'j': return 2;
	case 'k': return 3;
	}
}

static inline const char *
from_ord(char n)
{
	switch (n) {
	case 0: return "1";
	case 1: return "i";
	case 2: return "j";
	case 3: return "k";
	case 4: return "-1";
	case 5: return "-i";
	case 6: return "-j";
	case 7: return "-k";
	}
}

static inline char
table_index(char row, char col)
{
	return row * TABLE_WIDTH + col;
}

void
build_tables(void)
{
	for (int a = 0; a < 8; a++) {
		for (int b = 0; b < 8; b++) {
			char c = MULTIPLICATION_TABLE[table_index(a, b)];
			DIVISION_TABLE_B[table_index(c, b)] = a;
			DIVISION_TABLE_A[table_index(c, a)] = b;
		}
	}
}

static inline char
mult(char a, char b)
{
	return MULTIPLICATION_TABLE[a * TABLE_WIDTH + b];
}

static inline char
div_a(char c, char a)
{
	return DIVISION_TABLE_A[c * TABLE_WIDTH + a];
}

void
print_table(void)
{
	for (int a = 0; a < 8; a++) {
		for (int b = 0; b < 8; b++) {
			std::cout << from_ord(a) << " x " << from_ord(b) << " = "
				  << from_ord(mult(a, b)) << "\n";
		}
	}
}

int
is_ijk(char product, const std::vector<char> &digits)
{
	char left_i = to_ord('1'), right_jk = product;
	for (int j = 0; j < digits.size(); j++) {
		left_i = mult(left_i, digits[j]);
		right_jk = div_a(right_jk, digits[j]);
		if (left_i == I && right_jk == JK) {
			char left_j = to_ord('1'), right_k = right_jk;
			for (int k = j + 1; k < digits.size(); k++) {
				left_j = mult(left_j, digits[k]);
				right_k = div_a(right_k, digits[k]);
				if (left_j == J && right_k == K) {
					return 1;
				}
			}
		}
	}

	return 0;
}

int
main(int argc, const char **argv)
{
	int test_count;

	I = to_ord('i');
	J = to_ord('j');
	K = to_ord('k');
	JK = mult(J, K);
	IJK = mult(I, JK);

	build_tables();
	std::cin >> test_count;

	for (int i = 0; i < test_count; i++) {
		int char_count, repeats;
		std::cin >> char_count;
		std::cin >> repeats;

		std::string line;
		std::getline(std::cin, line);
		std::getline(std::cin, line);

		char c, product = to_ord('1');
		std::vector<char> digits;
		std::istringstream linestream(line);

		for (int j = 0; j < repeats; j++) {
			while (linestream >> c) {
				char ord = to_ord(c);
				product = mult(product, ord);
				digits.push_back(ord);
			}
			linestream.clear();
			linestream.seekg(0, linestream.beg);
		}

		const char *result = (product == IJK && is_ijk(product, digits)) ? "YES": "NO";
		std::cout << "Case #" << (i + 1) << ": " << result << "\n";
	}

	return 0;
}
