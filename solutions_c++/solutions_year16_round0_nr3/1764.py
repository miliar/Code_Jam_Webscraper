#include <iostream>
#include <cstdlib>
using namespace std;

void print_dd(int val, int n){
	for (int mask = 1 << n-1; mask; mask >>= 1)
		cout << ( ( val & mask ) ? "11" : "00" );
}

int main(int argc, char** argv){
	int mag = atoi(argv[1]), cnt = atoi(argv[2]);

	cout << "Case #1:\n";
	for (int i = 0; i < cnt; i++){
		cout << "1";
		print_dd(i, mag / 2 - 1);
		cout << "1";

		for (int j = 3; j <= 11; j++)
			cout << " " << j;
		cout << '\n';
	}
	return 0;
}
