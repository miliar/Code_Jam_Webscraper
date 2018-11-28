#include<bits/stdc++.h>
using namespace std;

#define DEBUGN	1

void breakdown( int x, bool* hash ) { 
	while( x > 0 ) { 
		hash[x%10] = true;
		x /= 10;
	}
}

bool all_covered( bool* hash) {
	int sum = 0;
	for( int i = 0; i < 10; ++i ) { 
		sum += hash[i];
	}
	return ( sum == 10 ? true: false );
}

int main() { 

	freopen("input.in", "r", stdin);
#ifndef DEBUG
	freopen("output.txt", "w", stdout);
#endif

	int t;	cin>>t;
	bool* hash = (bool*) malloc( 10 * sizeof(bool));

	for( int tt=1; tt<=t; ++tt) {

		bool found = false;
		memset(hash, 0, sizeof(bool) * 10 );
		int x;	cin>>x;
		int num = 0; 

		for( int n=0; n < 1000; ++n ) {
			num += x;
			breakdown(num, hash);
			if( all_covered(hash) ) {
				cout<<"Case #"<<tt<<": "<<num<<endl;
				found = true;
				break;
			}
		}

		if( not found ) { 
			if( x==0 ) { 
				cout<<"Case #"<<tt<<": "<<"INSOMNIA"<<endl;
			} else { 
				cout<<"SHIT"<<endl;
			}
		}
	}
	return 0;
}