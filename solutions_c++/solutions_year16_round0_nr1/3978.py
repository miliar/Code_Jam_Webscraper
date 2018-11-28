#include <bits/stdc++.h>

typedef long long lld;

using namespace std;

bool memory[10];
int counter = 0;

void fill( int n ){
	while( n > 0 ){
		int d = n % 10;
		
		if( !memory[d] ){
			memory[d] = 1;
			++counter;
		}
		
		n /= 10;
	}
}

int main(){
	
	freopen( "in", "r", stdin );
	freopen( "out", "w", stdout );
	
	int t;
	cin >> t;
	
	for( int w = 1; w <= t; ++w ){
		int n;
		cin >> n;
		
		memset( memory, 0 , sizeof memory );
		
		counter = 0;
		cout << "Case #" << w << ": ";
		if( n == 0 ){
			cout << "INSOMNIA" << endl;
		}
		else{
			int i;
			for( i = n; i < 1000000000; i += n ){
				fill(i);
				if(counter >= 10){
					break;
				}
			}
			cout << i << endl;
		}
		
	}
	
	return 0;
}	
