#include<iostream>
using namespace std;

int main() {
	int t, T, i, j, r;
	int x[18], y[18];
	int a, flag, n;
	cin >> T;
	for( t = 1; t <= T; ++t ) {
		for( i = 0; i < 18; ++i ) x[i] = y[i] = 0;
		
		cin >> r;
		for( i = 1; i < r; ++i ) for(j = 0; j < 4; ++j ) cin >> a;
		for( i = 0; i < 4; ++i ) {
			cin >> a;
			++x[a];
		}
		for( i = r+1; i <= 4; ++i ) for(j = 0; j < 4; ++j ) cin >> a;
		
		cin >> r;
		for( i = 1; i < r; ++i ) for(j = 0; j < 4; ++j ) cin >> a;
		for( i = 0; i < 4; ++i ) {
			cin >> a;
			++y[a];
		}
		for( i = r+1; i <= 4; ++i ) for(j = 0; j < 4; ++j ) cin >> a;
		
		flag = 0;
		for( i = 1; i < 17; ++i ) {
			if( x[i] && y[i] ) {
				++flag;
				n = i;
			}
		}
		
		if( flag ) {
			if( flag == 1 ) cout << "Case #" << t << ": " << n << endl;
			else cout << "Case #" << t << ": Bad magician!\n";
		}
		else {
			cout << "Case #" << t << ": Volunteer cheated!\n";
		}
		
	}
	return 0;
}

