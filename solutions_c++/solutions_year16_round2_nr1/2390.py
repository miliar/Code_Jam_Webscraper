#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main(){

	int R;
	cin >> R;
	string input;
	getline(cin, input);

	for(int i = 1; i <= R; i++){
		int map[26];
		memset(map,0,sizeof(map));
		getline(cin, input);
		for(int j = 0; j < input.length(); j++){
			map[ input[j] - 'A']++;
		}
		int num[10];
		num[0] = map['Z'-'A'];
		num[6] = map['X'-'A'];
		num[8] = map['G'-'A'];
		num[2] = map['W'-'A'];
		num[3] = map['H'-'A'] - num[8];
		num[4] = map['R'-'A'] - num[3] - num[0];
		num[7] = map['S'-'A'] - num[6];
		num[5] = map['F'-'A'] - num[4];
		num[1] = map['O'-'A'] - num[2] - num[0] -num[4];
		num[9] = (map['N'-'A'] - num[7] - num[1]) / 2;

		string output;
		for(int j = 0; j < 10; j++)
			for(int k = 0; k < num[j]; k++)
				output += '0' + j;

		cout << "Case #" << i << ": " << output << endl;
	}
	return 0;
}

