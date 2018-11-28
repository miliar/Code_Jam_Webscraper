#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int arr[101];
int main() {
	int a, b, d, e;
	string c;
	cin >> a;

	for ( int i = 1; i <= a; ++i ) {
		cin >> b;
		cin >> c;
		d = 0;
		e = 0;

		for ( int j = 0; j <= b; ++j ) {
			if ( c.at(j) == '0' ) {
				if ( e == j ) {
					++d;
					++e;
				}
			}
			e += c.at(j) - 48;
		}

		arr[i] = d;
	}

	for ( int i = 1; i <= a; ++i ) {
		cout << "Case #" << i << ": " << arr[i] << endl;
	}

}