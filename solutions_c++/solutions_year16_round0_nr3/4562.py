#include <iostream>
#include <string>
#include <vector>
#include <bitset> 

using namespace std;

typedef long long ll;
ll bases[11][16];
ll num = 0b1000000000000001;
string numstr;
string out;
int nums = 50;
bool factorize(ll num) {
	for (ll i = 3; i <= sqrt((double)num); i += 2) {
		if (num%i == 0) {
			out += to_string(i)+' ';
			return true;
		}
	}
	return false;
}
ll calc(int base) {
	ll result = 0;
	for (int i = 0; i < 16; ++i) {
		result += (numstr[i] - '0')*bases[base][15 - i];
	}
	return result;
}
void check_number() {
	//base 2
	if (!factorize(num)) return;
	// bases not 2
	for (int i = 3; i < 11; ++i) {
		if (!factorize(calc(i))) return;
	}
	cout << out.substr(0, out.length() - 1) << '\n';
	nums--;
}
void initialize() {
	for (int i = 3; i < 11; ++i) bases[i][0] = 1;
	for (int i = 3; i < 11; ++i) {
		for (int j = 1; j < 16; ++j) {
			bases[i][j] = i*bases[i][j-1];
		}
	}
}


int main() {
	freopen("output.txt", "w", stdout);
	initialize();
	cout << "Case #1:\n";
	while (nums != 0) {
		bitset<16> numb(num);
		numstr = numb.to_string();
		out = numstr + ' ';
		check_number();
		num += 2;
	}

	return 0;
}