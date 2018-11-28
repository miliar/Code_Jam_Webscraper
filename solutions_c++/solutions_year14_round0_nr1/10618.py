#include <iostream>
using namespace std;

int main() {
	int n,e,c1[4],c2[4],tmp;
	
	cin >> n;
	
	for( int i = 1; i<=n; i++ ){
		for( int j = 0; j < 4; j++ ) c1[j] = c2[j] = 0;
		
		cin >> e;
		e--;
		
		for( int j = 0; j < 4; j++ ){
			if( j == e ){
				for( int k = 0; k < 4; k++ ) cin >> c1[k];
			}
			else{
				for( int k = 0; k < 4; k++ ) cin >> tmp;
			}
		}
		
		cin >> e;
		e--;
		
		for( int j = 0; j < 4; j++ ){
			if( j == e ){
				for( int k = 0; k < 4; k++ ) cin >> c2[k];
			}
			else{
				for( int k = 0; k < 4; k++ ) cin >> tmp;
			}
		}
		
		e = 0;
		int g;
		for( int h = 0; h < 4; h++ ){
			for( int j = 0; j < 4; j++ ){
				if( c1[h] == c2[j] ) {
					e++;
					g = c1[h];
				}
			}
		}
		
		cout << "Case #" << i << ": ";
		if( e == 1 ) cout << g << endl;
		else if( e > 1 ) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}