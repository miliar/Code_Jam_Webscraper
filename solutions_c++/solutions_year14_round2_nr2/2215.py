#include <iostream>

using namespace std;

int main()
{

	int t;
	cin >> t;


	for ( int  x = 1; x <= t; x++ ) {
		int a;
		int b;
		int k;

		cin >> a >> b >> k;
		
		if ( b > a ) {
			int t = b;
			b = a;
			a = t;
		}

		int ctr = 0;
		for ( int i = 0; i < a; i++) { 
			for ( int j = 0; j < b ; j++ ) {
				if ( (i&j) < k ) {
					ctr++;
					if ( i != j ) {
					//	ctr++;
					//	cout << j << "    " << i << endl;
						
					}
				//	cout << i << "    " << j << endl;
				}
			}
		}

		cout << "Case #" << x <<": " << ctr << endl;
	}

	return 0;
}
