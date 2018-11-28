#include <iostream>
#include <cstdlib>
#include <vector>
#define PB push_back
using namespace std;

int main()
{
	int CASES = 0;
	cin >> CASES;
	
	for( int i = 1 ; i <= CASES ; i++ ){
		cout << "Case #" << i << ": ";
		vector<char> xl,ol,d1(4),d2(4);
		vector<int> xc(4,0),oc(4,0);
		char aux = 'a';
		bool flag = false,loop = false;
		xl.clear(); ol.clear();
		int j = 0;
		for( j = 0 ; j < 16 ; j++ ){
			cin >> aux;
			if( j % 4 == 0 && j != 0 ){
				if( xl.size() == 4 ){
					cout << "X won" << endl; loop = true; break;
				}
				if( ol.size() == 4 ){
					cout << "O won" << endl; loop = true; break;
				}
				xl.clear();
				ol.clear();
			}
			if( aux == 'X' || aux == 'T' ){ xl.PB( 'X' ); }
			if( aux == 'O' || aux == 'T' ){ ol.PB( 'O' ); }
			if( ( j % 5 ) == 0 ) d1[ j / 4 ] = aux;
			if( ( j % 3 ) == 0 && j < 15 ) d2[ j / 4 ] = aux;
			if( aux == 'X' || aux == 'T' ) xc[ j % 4 ]++;
			if( aux == 'O' || aux == 'T' ) oc[ j % 4 ]++;
			if( aux == '.' ) flag = true;
		
		}

		if( loop ){
			for( int z = j ; z < 15 ; z++ ) cin >> aux;
			continue;
		}
		if ( xc[ 0 ] == 4 || xc[ 1 ] == 4 || xc[ 2 ] == 4 || xc[ 3 ] == 4 ){
			cout << "X won" << endl;
			continue;
		}else if ( oc[ 0 ] == 4 || oc[ 1 ] == 4 || oc[ 2 ] == 4 || oc[ 3 ] == 4 ){
			cout << "O won" << endl;
			continue;
		}

		int count = 1;
		aux = d1[ 0 ];

		for( int z = 1 ; z < d1.size() ; z++ ){
			if( aux != d1[ z ] && d1[ z ] != 'T' || aux == '.' ) break;
			count++;
		}
		if( count == 4 ){
			cout << aux << " won" << endl;
			continue;
		}

		count = 1;
		aux = d2[ 0 ];
		for( int z = 1 ; z < d2.size() ; z++ ){
			if( aux != d2[ z ] && d2[ z ] != 'T' || aux == '.' ) break;
			count++;
		}
		if( count == 4 ){
			cout << aux << " won" << endl;
			continue;
		}
		if( flag ){
			cout << "Game has not completed" << endl;
			continue;
		}else cout << "Draw" << endl;
	}
	return 0;
}
