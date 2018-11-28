

#include <iostream>

#define MAXN 1001

using namespace std;


char ch;
int T, N;
int list[MAXN];

int main() {

	cin >> T;

	for (int j = 0; j < T; ++j) {
	    
	    cin >> N;
	    for (int i = 0; i <= N; ++i){
	 		cin >> ch;
	 		list[i] = ch - '0';   	
	    }

	    int up = list[0];
	    int sol = 0;

	    for (int i = 1; i <= N; ++i) {
			if (up >= i || list[i] == 0) {
				up += list[i];
			}
			else {
				sol += i - up;
				up += list[i] + (i - up);
			}	    		
	    }

	    cout << "Case #" << j + 1 << ": " << sol << endl; 
	}


	return 0;
}