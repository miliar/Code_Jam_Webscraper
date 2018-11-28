#include <iostream>
#include <cstdio>
using namespace std;
     
int main() {
	int T;
	cin >> T;
	int count = 0;
	while( T-- ) {
		double C, F, X, y=0;
		int n = 0;
		count++;
		cin >> C >> F >> X;
		double yy, t = 0;
		y = t + ( X / ( 2 + ( n * F )));
		t = C / ( 2 + ( n * F ));
		yy= t + (X / ( 2 + ( ( n + 1 ) * F )));
		while( yy < y ) {
			n++;
			y = t + ( X / ( 2 + ( n * F )));
			t = t + ( C / ( 2 + ( n * F )));
			yy= t + ( X / ( 2 + ( ( n + 1 ) * F )));
		}
		cout << "case #" << count << ": ";
		printf( "%.7lf\n", y);
    }
    return 0;
}
