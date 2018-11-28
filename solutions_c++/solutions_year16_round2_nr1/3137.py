#include <iostream>
#include <vector>
#include <map>
#include <string>
# include <algorithm>

using namespace std;

void printmap(map<char, int> mp) {
	map<char, int>::iterator it = mp.begin();

	while (it != mp.end()) {
		cout << it->first << " " << it->second << endl;
		it++;
	}
}

int main() {

	int n;
	cin >> n;
	map<char, int> mp;
	map<char, int>:: iterator it;
	std::vector<int> v;
	for (int p = 0; p < n; p++) {
		string s;
		cin >> s;

		int l = s.length();
		//make a map first

		for (int m = 0; m < l; m++) {
			it = mp.find(s[m]);
			if (it != mp.end()) {
				mp[s[m]]++;
			}
			else {
				mp[s[m]] = 1;
			}

		}

		//printmap(mp);

		// go over map do the first iteration and do the first iteration
		// check for z =0, W= 2, u=4, x=six, g=eight

		it = mp.find('Z');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['Z'], 0);
			mp['E'] -= mp['Z'];
			mp['R'] -= mp['Z'];
			mp['O'] -= mp['Z'];
			mp['Z'] = 0;
		}

		it = mp.find('W');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['W'], 2);
			mp['T'] -= mp['W'];
			mp['O'] -= mp['W'];
			mp['W'] = 0;
		}

		it = mp.find('U');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['U'], 4);
			mp['F'] -= mp['U'];
			mp['O'] -= mp['U'];
			mp['R'] = 0;
		}

		it = mp.find('X');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['X'], 6);
			mp['I'] -= mp['X'];
			mp['S'] -= mp['X'];
			mp['X'] = 0;
		}

		it = mp.find('G');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['G'], 8);
			mp['E'] -= mp['G'];
			mp['I'] -= mp['G'];
			mp['H'] -= mp['G'];
			mp['T'] -= mp['G'];
			mp['G'] = 0;
		}


		//now check for  o =
		it = mp.find('O');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['O'], 1);
			mp['E'] -= mp['O'];
			mp['N'] -= mp['O'];
			mp['O'] = 0;
		}


		it = mp.find('T');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['T'], 3);
			mp['H'] -= mp['T'];
			mp['R'] -= mp['T'];
			mp['E'] -= mp['T'];
			mp['E'] -= mp['T'];
			mp['T'] = 0;
		}

		it = mp.find('F');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['F'], 5);
			mp['I'] -= mp['F'];
			mp['V'] -= mp['F'];
			mp['E'] -= mp['F'];
			mp['F'] = 0;
		}

		it = mp.find('S');
		if (it != mp.end()) {
			//zero is in number
			v.insert(v.begin(), mp['S'], 7);
			mp['E'] -= mp['S'];
			mp['V'] -= mp['S'];
			mp['E'] -= mp['S'];
			mp['N'] -= mp['S'];
			mp['S'] = 0;
		}

		it = mp.find('N');
		if (it != mp.end()) {
			v.insert(v.begin(), mp['N']/2, 9);
			mp['I'] -= mp['N'] / 2;
			mp['E'] -= mp['N'] / 2;
			mp['N'] = 0;

		}


		sort(v.begin(), v.end());
		cout << "Case #" << (p + 1) << ": ";
		for (int q = 0; q < v.size(); q++) {
			cout << v[q];
		}
		cout << endl;

		//clear vector
		v.clear();
		//clear map
		mp.clear();
	}

}