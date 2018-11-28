#include <bits/stdc++.h>

using namespace std;

const vector<string> num = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		string in;
		cin >> in;

		map<char, int> letters;
		//letters INIT
		letters['Z'] = 0;
		letters['E'] = 0;
		letters['R'] = 0;
		letters['O'] = 0;
		letters['N'] = 0;
		letters['T'] = 0;
		letters['W'] = 0;
		letters['H'] = 0;
		letters['F'] = 0;
		letters['U'] = 0;
		letters['I'] = 0;
		letters['V'] = 0;
		letters['S'] = 0;
		letters['X'] = 0;
		letters['G'] = 0;

		for(auto x : in) {
			letters[x]++;
		}

		vector<int> res;
		//ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE
		while(letters['X'] > 0) {
			res.push_back(6);
			letters['S']--;
			letters['I']--;
			letters['X']--;
		}
		
		while(letters['Z'] > 0) {
			res.push_back(0);
			letters['Z']--;
			letters['E']--;
			letters['R']--;
			letters['O']--;
		}

		while(letters['W'] > 0) {
			res.push_back(2);
			letters['T']--;
			letters['W']--;
			letters['O']--;
		}

		while(letters['G'] > 0) {
			res.push_back(8);
			letters['E']--;
			letters['I']--;
			letters['G']--;
			letters['H']--;
			letters['T']--;
		}

		while(letters['U'] > 0) {
			res.push_back(4);
			letters['F']--;
			letters['O']--;
			letters['U']--;
			letters['R']--;
		}

		while(letters['S'] > 0) {
			res.push_back(7);
			letters['S']--;
			letters['E']--;
			letters['V']--;
			letters['E']--;
			letters['N']--;
		}

		while(letters['V'] > 0) {
			res.push_back(5);
			letters['F']--;
			letters['I']--;
			letters['V']--;
			letters['E']--;
		}

		while(letters['H'] > 0) {
			res.push_back(3);
			letters['T']--;
			letters['H']--;
			letters['R']--;
			letters['E']--;
			letters['E']--;
		}

		while(letters['O'] > 0) {
			res.push_back(1);
			letters['O']--;
			letters['N']--;
			letters['E']--;
		}

		while(letters['N'] > 0) {
			res.push_back(9);
			letters['N']--;
			letters['I']--;
			letters['N']--;
			letters['E']--;
		}


		sort(res.begin(), res.end());
		cout << "Case #" << t << ": ";
		for(auto x : res) cout << x;
		cout << "\n";
	}

	return 0;
}
