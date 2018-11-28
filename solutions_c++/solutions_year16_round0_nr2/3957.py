#include <iostream>
#include <string>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int T;
string a;

int main(){
	
	optimizar_io
	cin >> T;
	for( int t = 1; t <= T; t++ ){
		cout << "Case #" << t << ": ";
		
		cin >> a;
		int cont = 0;
		for( int i = 1; i < a.size(); i++ )
			if( a[i] != a[i - 1] )
				cont++;
		if( a[ a.size() - 1] == '-' )
			cont++;
		cout << cont << "\n";
	}
	
}