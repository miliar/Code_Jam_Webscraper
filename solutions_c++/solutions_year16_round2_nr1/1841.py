//#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <list>
#include <string>

#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORI(i, a, n) for(int i = (int)(a); i < (int)(n); i++)


int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "wb", stdout);

	int numOfTestcases;
	std::cin >> numOfTestcases;

	FOR(i, numOfTestcases)
	{
		std::cout << "Case #" << (i + 1) << ": ";

		std::string s;
		std::cin >> s;

		int numCount[10];
		FOR(i, 10)
		{
			numCount[i] = 0;
		}

		int letterCount[100];
		FOR(i, 100)
		{
			letterCount[i] = 0;
		}

		FOR(i, (int)s.length())
		{
			letterCount[s[i]]++;
		}


		numCount[0] = letterCount['Z'];
		FOR(i, letterCount['Z'])
		{
			letterCount['E']--;
			letterCount['R']--;
			letterCount['O']--;
		}
		letterCount['Z'] = 0;

		numCount[2] = letterCount['W'];
		FOR(i, letterCount['W'])
		{
			letterCount['T']--;
			letterCount['O']--;
		}
		letterCount['W'] = 0;

		numCount[4] = letterCount['U'];
		FOR(i, letterCount['U'])
		{
			letterCount['F']--;
			letterCount['O']--;
			letterCount['R']--;
		}
		letterCount['U'] = 0;

		numCount[5] = letterCount['F'];
		FOR(i, letterCount['F'])
		{
			letterCount['I']--;
			letterCount['V']--;
			letterCount['E']--;
		}
		letterCount['F'] = 0;

		numCount[6] = letterCount['X'];
		FOR(i, letterCount['X'])
		{
			letterCount['S']--;
			letterCount['I']--;
		}
		letterCount['X'] = 0;

		numCount[7] = letterCount['V'];
		FOR(i, letterCount['V'])
		{
			letterCount['S']--;
			letterCount['E']--;
			letterCount['E']--;
			letterCount['N']--;
		}
		letterCount['V'] = 0;

		numCount[8] = letterCount['G'];
		FOR(i, letterCount['G'])
		{
			letterCount['E']--;
			letterCount['I']--;
			letterCount['H']--;
			letterCount['T']--;
		}
		letterCount['G'] = 0;

		numCount[9] = letterCount['I'];
		FOR(i, letterCount['I'])
		{
			letterCount['N']--;
			letterCount['N']--;
			letterCount['E']--;
		}
		letterCount['I'] = 0;

		numCount[1] = letterCount['O'];
		FOR(i, letterCount['O'])
		{
			letterCount['N']--;
			letterCount['E']--;
		}
		letterCount['O'] = 0;

		numCount[3] = letterCount['T'];
		FOR(i, letterCount['T'])
		{
			letterCount['H']--;
			letterCount['R']--;
			letterCount['E']--;
			letterCount['E']--;
		}
		letterCount['T'] = 0;

		FOR(i, 10)
		{
			FOR(j, numCount[i])
			{
				std::cout << i;
			}
		}
		std::cout << std::endl;
	}

	return 0;
}