#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main (){
	int ncases;
	cin >> ncases;
	cin.ignore();
	string line;
	for(int i = 1; i <= ncases; i++){
		int letters[26] = {0};
		int count[10] = {0};
		getline(cin,line);
		for(auto letter : line){
			letters[(int)(letter-'A')] += 1;
		}
		count[0] = letters['Z'-'A'];
		letters['E'-'A'] -= letters['Z'-'A'];
		letters['O'-'A'] -= letters['Z'-'A'];
		letters['R'-'A'] -= letters['Z'-'A'];
		letters['Z'-'A'] -= letters['Z'-'A'];

		count[6] = letters['X'-'A'];
		letters['S'-'A'] -= letters['X'-'A'];
		letters['I'-'A'] -= letters['X'-'A'];
		letters['X'-'A'] -= letters['X'-'A'];

		count[2] = letters['W'-'A'];
		letters['T'-'A'] -= letters['W'-'A'];
		letters['O'-'A'] -= letters['W'-'A'];
		letters['W'-'A'] -= letters['W'-'A'];

		count[4] = letters['U'-'A'];
		letters['F'-'A'] -= letters['U'-'A'];
		letters['O'-'A'] -= letters['U'-'A'];
		letters['R'-'A'] -= letters['U'-'A'];
		letters['U'-'A'] -= letters['U'-'A'];

		count[8] = letters['G'-'A'];
		letters['E'-'A'] -= letters['G'-'A'];
		letters['I'-'A'] -= letters['G'-'A'];
		letters['H'-'A'] -= letters['G'-'A'];
		letters['T'-'A'] -= letters['G'-'A'];
		letters['G'-'A'] -= letters['G'-'A'];

		count[3] = letters['T'-'A'];
		letters['R'-'A'] -= letters['T'-'A'];
		letters['E'-'A'] -= 2*letters['T'-'A'];
		letters['T'-'A'] -= letters['T'-'A'];

		count[5] = letters['F'-'A'];
		letters['I'-'A'] -= letters['F'-'A'];
		letters['V'-'A'] -= letters['F'-'A'];
		letters['E'-'A'] -= letters['F'-'A'];
		letters['F'-'A'] -= letters['F'-'A'];

		count[9] = letters['I'-'A'];
		letters['N'-'A'] -= 2*letters['I'-'A'];
		letters['E'-'A'] -= letters['I'-'A'];
		letters['I'-'A'] -= letters['I'-'A'];

		count[7] = letters['S'-'A'];
		letters['E'-'A'] -= 2*letters['S'-'A'];
		letters['V'-'A'] -= letters['S'-'A'];
		letters['N'-'A'] -= letters['S'-'A'];
		letters['S'-'A'] -= letters['S'-'A'];

		count[1] = letters['O'-'A'];
		cout << "Case #" << i << ": "; 
		while(count[0]-- > 0) cout << '0';
		while(count[1]-- > 0) cout << '1';
		while(count[2]-- > 0) cout << '2';
		while(count[3]-- > 0) cout << '3';
		while(count[4]-- > 0) cout << '4';
		while(count[5]-- > 0) cout << '5';
		while(count[6]-- > 0) cout << '6';
		while(count[7]-- > 0) cout << '7';
		while(count[8]-- > 0) cout << '8';
		while(count[9]-- > 0) cout << '9';

		cout << endl;
	}

	return 0;
}


