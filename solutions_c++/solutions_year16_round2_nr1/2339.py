
#include<iostream>
#include<string>
#include<map>
using namespace std;


int amount[10];

int main()
{
	std::ios_base::sync_with_stdio(true);


	int t;
	cin >> t;

	string s;
	getline(cin, s);

	for (int k = 1; k <= t; k++) {

		for (int l = 0; l < 10; l++) {
			amount[l] = 0;
		}

		std::map<char, int> m;

		getline(cin, s);

		for (int l = 0; l < s.size(); l++) {
			m[s[l]]++;
		}

		int zeroes = m['Z'];
		amount[0] = zeroes;
		m['E'] -= zeroes;
		m['R'] -= zeroes;
		m['O'] -= zeroes;

		int sixes = m['X'];
		amount[6] = sixes;
		m['S'] -= sixes;
		m['I'] -= sixes;

		int eights = m['G'];
		amount[8] = eights;
		m['E'] -= eights;
		m['I'] -= eights;
		m['H'] -= eights;
		m['T'] -= eights;
		
		int threes = m['H'];
		amount[3] = threes;
		m['R'] -= threes;
		m['T'] -= threes;

		int fours = m['R'];
		amount[4] = fours;
		m['F'] -= fours;
		m['O'] -= fours;

		int fives = m['F'];
		amount[5] = fives;
		m['I'] -= fives;
		m['V'] -= fives;

		int sevens = m['V'];
		amount[7] = sevens;

		int nines = m['I'];
		amount[9] = nines;

		int twos = m['T'];
		amount[2] = twos;
		m['O'] -= twos;

		int ones = m['O'];
		amount[1] = ones;

		cout << "Case #" << k << ": ";

		for (int l = 0; l < 10; l++) {

			for (int g = 0; g < amount[l]; g++) {
				cout << l;
			}
		}
		cout << endl;

	}
	return 0;
}

