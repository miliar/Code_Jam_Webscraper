#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	string pstack;


	for(int t = 1; t <= T; t++){
		// Get the pancake stack		
		//pstack.clear();
		cin >> pstack;

		// Process it
		int x = 0;

		// Case of only one pancake
		if( (int)pstack.size()==0 && pstack[0] == '-') 
			x++;
		else  {
			// General case: start from one if alst pancake is -
			if( pstack[(int)pstack.size()-1] == '-') 
				x=1;
			// General case: count transitions
			for (int c=0; c<(int)pstack.size()-1; c++) {
				if( pstack[c] != pstack[c+1])
					x++;
			}		
		}		
		cout << "Case #" << t << ": " << x << endl;
	}
	return 0;
}
