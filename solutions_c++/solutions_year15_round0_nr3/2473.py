#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <fstream>
#include <cassert>

#define INF 999999999999999999LL
#define MOD 1000000007
#define MAX 201000
#define ALL 50
#define DEBUG false

using namespace std;

int n,t,k;
map<char, vector<int> > M;

int tab[4][4] = {
	{1, 2, 3, 4},
	{2, -1, 4, -3},
	{3, -4, -1, 2},
	{4, 3, -2, -1}
};

char changeToChar(int x)
{
	if (x == 1)
		return '1';
	else if (x == 2)
		return 'i';
	else if (x == 3)
		return 'j';
	else
		return 'k';
}

int changeToInt(char x)
{
	if (x == '1')
		return 1;
	else if (x == 'i')
		return 2;
	else if (x == 'j')
		return 3;
	else
		return 4;
}

int main()
{
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test) {
		scanf("%d %d", &n, &k);
		string str;
		cin >> str;
		string pom = str;
		for (int i = 0; i < k-1; ++i) {
			pom += str;
		}
		str = pom;
		n = str.length();

		// if (test == 6 || test == 17 || test == 36 || test == 69) {
		// 	cout << n << ";" << k << ";" << str << endl;
		// }

		char first = str[0], second;
		bool minus = false, ok = false;
		int firstFind = -1, secondFind = -1, thirdFind = -1;

		if (first == 'i') {
			//M[first].push_back(0);
			firstFind = 0;
			first = '1';
		}

		int multi;
		for (int i = 1; i < n; ++i) {
			second = str[i];

			multi = tab[changeToInt(first)-1][changeToInt(second)-1];
			//cout << i << " -> " << multi << "; [" << first << ";" << second << "]" << endl;
			if (minus)
				multi = -multi;

			if (multi < 0) {
				multi = -multi;
				minus = true;
			} else {
				minus = false;
			}

			first = changeToChar(abs(multi));

			if (firstFind >= 0) {
				if (secondFind == -1) {
					if (!minus && changeToChar(multi) == 'j') { // dodajemy pozycje na ktorych moga wystapic (i lub j lub k)
						secondFind = i;
						first = '1';
					}
				}
			} else {
				if (!minus && changeToChar(multi) == 'i') { // dodajemy pozycje na ktorych moga wystapic (i lub j lub k)
					firstFind = i;
					first = '1';
				}
			}
		}

		//cout << firstFind << ";" << secondFind << ";" << endl;


		if (!minus && changeToChar(multi) == 'k' && secondFind >= 0) { // dodajemy pozycje na ktorych moga wystapic (i lub j lub k)
			thirdFind = 101;
		}

		// first = str[0]; minus = false;
		// for (int i = 1; i < n; ++i) {
		// 	second = str[i];

		// 	multi = tab[changeToInt(first)-1][changeToInt(second)-1];
		// 	if (minus)
		// 		multi = -multi;

		// 	if (multi < 0) {
		// 		multi = -multi;
		// 		minus = true;
		// 	} else {
		// 		minus = false;
		// 	}

		// 	first = changeToChar(abs(multi));
		// }

		// if (minus && multi == 1) {
		// 	cout << "YESSS: ";
		// }

		if (thirdFind > 0) {
			ok = true;
		}

		string res = "NO";
		if (ok) {
			res = "YES";
		}

		cout << "Case #" << test << ": " << res << endl;
	}

	return 0;
}
