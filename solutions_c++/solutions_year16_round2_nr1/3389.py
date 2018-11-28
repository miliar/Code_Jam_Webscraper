#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>
#include <cassert>
#include <bitset>

using namespace std;

void
PrintResult(int i, const string& res)
{
	cout << "Case #" << i << ": " << res << endl;
}

void Minus(map<char, int>& s, int n, const char* str) {
	do {
		if (*str == 0) break;
		s[*str] -= n;
		++str;
	} while (true);
}

string
Solve(const string& number)
{
	map<char, int> num2n;
	for (char c : number) {
		num2n[c]++;
	}
	int digits[10] = {};
	int zero = num2n['Z'];
	digits[0] = zero;
	Minus(num2n, zero, "ZERO");

	int two = num2n['W'];
	digits[2] = two;
	Minus(num2n, two, "TWO");

	int four = num2n['U'];
	digits[4] = four;
	Minus(num2n, four, "FOUR");

	int six = num2n['X'];
	digits[6] = six;
	Minus(num2n, six, "SIX");

	int eight = num2n['G'];
	digits[8] = eight;
	Minus(num2n, eight, "EIGHT");

	int five = num2n['F'];
	digits[5] = five;
	Minus(num2n, five, "FIVE");

	int seven = num2n['V'];
	digits[7] = seven;
	Minus(num2n, seven, "SEVEN");

	int nine = num2n['I'];
	digits[9] = nine;
	Minus(num2n, nine, "NINE");

	int three = num2n['H'];
	digits[3] = three;
	Minus(num2n, three, "THREE");

	int one = num2n['O'];
	digits[1] = one;
	Minus(num2n, one, "ONE");

	string ss;
	for (int i = 0; i < 10; ++i) {
		char c = i + '0';
		for (int j = 0; j < digits[i];++j) {
			ss.push_back(c);
		}
	}
	return ss;

}
int
main()
{
	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	ofstream err("log.txt");
	cerr.rdbuf(err.rdbuf());
	
	int T;
	cin >> T;

	string number;
	for (int i = 1; i <= T; ++i) {
		do {
			getline(cin, number);
		} while (number.empty());
		auto r = Solve(number);
		PrintResult(i, r);
	}

	return 0;
}
