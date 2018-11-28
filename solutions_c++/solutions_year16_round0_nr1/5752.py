#include "iostream"
#include "string"

using namespace  std;

int main() {

	int T;
	cin >> T;

	int i = 0, N, R, b;
	while ( T-- ) {
		i++;

		cin >> N;
		R = N;
		b = 0;

		string s;
		while( N ) {
			s = to_string( R );
			for (string::iterator it = s.begin(); it != s.end(); ++it ) {
				b |= ( 1 << (*it - '0') );
			}
			if ( b == 1023 ) break;
			R += N;
		}

		cout << "Case #" << i << ": ";
		if ( N == 0)
			cout << "INSOMNIA\n";
		else
			cout << R << "\n";
	}

	return 0;
}