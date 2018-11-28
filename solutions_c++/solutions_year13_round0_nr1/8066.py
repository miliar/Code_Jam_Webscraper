#include <iostream> 
#include <vector> 

using namespace std; 
int main() {

	int T; 
	cin >> T; 

	for(int i=0;i<T;i++) { 
		int b[4][4] ;

		int result = -1; 
		bool processed = false; 
		bool sawdot = false; 

		// input 
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				char c; 
				cin >> c; 
				switch(c) { 
					case '.':
						b[j][k] = 0; 
						break; 
					case 'T':
						b[j][k] = 0; 
						break; 
					case 'X': 
						b[j][k] = 3; 
						break; 
					case 'O': 
						b[j][k] = 7; 
						break; 
					default: 
						b[j][k] = 999; // shud never happen 
						break; 
					}
				if(c == '.') 
					sawdot = true; 
				}
			}

		int r[4] = {0}, c[4] = {0}, d1 = 0, d2 = 0; 

		if(!processed) 
			{
			// r's 
			for(int j=0;j<4;j++) {
				r[j] += b[j][0] + b[j][1] + b[j][2] + b[j][3]; 			
				}

			//c's
			for(int j=0;j<4;j++) {
				c[j] += b[0][j] + b[1][j] + b[2][j] + b[3][j]; 			
				}

			// d1 
			d1 = b[0][0] + b[1][1] + b[2][2] + b[3][3]; 

			// d2 
			d2 = b[0][3] + b[1][2] + b[2][1] + b[3][0]; 

			for(int p=0;p<4;p++) {  
				if( (r[p] == 9) || (r[p] == 12) || (c[p] == 9) || (c[p] == 12) || (d1 == 9) || (d1 == 12) || (d2 == 9) || (d2 == 12))
					{
					processed = true; 
					result = 0;  
					}
				} 

			for(int p=0;p<4;p++) {  
				if( (r[p] == 21) || (r[p] == 28) || (c[p] == 21) || (c[p] == 28) || (d1 == 21) || (d1 == 28) || (d2 == 21) || (d2 == 28))
					{
					processed = true; 
					result = 1;  
					}
				}

			if(!processed) { 
				processed = true;
				if(sawdot) 	
					result = 3; 
				else 
					result = 2; 
				}
			} 

		// output
		cout << "Case #" << (i+1) << ": "; 
		switch(result) {
			case 0:
				cout << "X won" << endl; 
				break; 
			case 1:
				cout << "O won" << endl; 
				break; 
			case 2: 
				cout << "Draw" << endl; 
				break; 
			case 3: 
				cout << "Game has not completed" << endl; 
				break; 
			default: 
				cout << ".. err should not have been printed ever" << endl; 
				break; 
			} 
		}

	return 0; 
	}
