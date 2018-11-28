#include <iostream>
#include <algorithm>
#include <string>
#include <array>

using namespace std;

void do_case() {
	string s;
	cin >> s;
	array<int,26> occur = { 0 };
	for( char c : s ) {
		++occur[c-'A'];
	}

	array<int,10> res = { 0 };
	res[0] = occur['z'-'a'];
	occur['z'-'a'] -= res[0];
	occur['e'-'a'] -= res[0];
	occur['r'-'a'] -= res[0];
	occur['o'-'a'] -= res[0];

	res[2] = occur['w'-'a'];
	occur['t'-'a'] -= res[2];
	occur['w'-'a'] -= res[2];
	occur['o'-'a'] -= res[2];

	res[6] = occur['x'-'a'];
	occur['s'-'a'] -= res[6];
	occur['i'-'a'] -= res[6];
	occur['x'-'a'] -= res[6];

	res[8] = occur['g'-'a'];
	occur['e'-'a'] -= res[8];
	occur['i'-'a'] -= res[8];
	occur['g'-'a'] -= res[8];
	occur['h'-'a'] -= res[8];
	occur['t'-'a'] -= res[8];

	res[7] = occur['s'-'a'];
	occur['s'-'a'] -= res[7];
	occur['e'-'a'] -= res[7];
	occur['v'-'a'] -= res[7];
	occur['e'-'a'] -= res[7];
	occur['n'-'a'] -= res[7];

	res[5] = occur['v'-'a'];
	occur['f'-'a'] -= res[5];
	occur['i'-'a'] -= res[5];
	occur['v'-'a'] -= res[5];
	occur['e'-'a'] -= res[5];

	res[4] = occur['f'-'a'];
	occur['f'-'a'] -= res[4];
	occur['o'-'a'] -= res[4];
	occur['u'-'a'] -= res[4];
	occur['r'-'a'] -= res[4];

	res[3] = occur['h'-'a'];
	occur['t'-'a'] -= res[3];
	occur['h'-'a'] -= res[3];
	occur['r'-'a'] -= res[3];
	occur['e'-'a'] -= res[3];
	occur['e'-'a'] -= res[3];

	res[9] = occur['i'-'a'];
	occur['n'-'a'] -= res[9];
	occur['i'-'a'] -= res[9];
	occur['n'-'a'] -= res[9];
	occur['e'-'a'] -= res[9];

	res[1] = occur['o'-'a'];
	occur['o'-'a'] -= res[1];
	occur['n'-'a'] -= res[1];
	occur['e'-'a'] -= res[1];

	for( int i=0; i<10; ++i ) {
		for( int j=0; j<res[i]; ++j ) {
			cout << i;
		}
	}
}

int main() {
	unsigned int T;
	cin >> T;

	for( unsigned int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": ";
		do_case();
		cout << endl;
	}
}
