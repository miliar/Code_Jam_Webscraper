#include <iostream>
#include <algorithm>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int T;
int vis[14];
int n;

int main(){
	
	optimizar_io
	
	cin >> T;
	for( int t = 1; t <= T; t++ ){
		cout << "Case #" << t << ": ";
		
		cin >> n;
		
		if( n == 0 ){
			cout << "INSOMNIA\n";
			continue;
		}
		
		int cont = 0, aux = n;
		fill( vis, vis + 11, 0 );
		while( cont < 10 ){
			
			int act = n;
			while( act ){
				if( !vis[act % 10] ){
					vis[act % 10]++;
					cont++;
				}
				act /= 10;
			}
			
			if( cont == 10 ){
				cout << n << "\n";
				break;
			}
			
			n += aux;
		}
	
	}
	
	return 0;
	
}