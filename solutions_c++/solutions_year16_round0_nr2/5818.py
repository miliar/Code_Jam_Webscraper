#include <iostream>

using namespace std;


int main() {
	int T;
	cin >> T;

	string S;
	char c;
	int i = 0, R;
	while ( T-- ) {
		i++;

		cin >> S;

		R = 0;
		c = 0;
		for (string::iterator it = S.begin(); it != S.end(); ++it ) {
			if ( c != *it ) {
				c = *it;
				R ++;
			}
		}

		if ( *S.rbegin() == '+' )
			R --;

		cout << "Case #" << i << ": " << R << "\n";
	}

	return 0;
}