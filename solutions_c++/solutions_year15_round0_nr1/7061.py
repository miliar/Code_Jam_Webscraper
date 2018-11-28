#include <stdio.h>
#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

int main() {
	int T;
	
	short int S[1001];
	int smax;
	char input[1100], *inp;
	int ta,n,slevel,pos;
	
	cin >> T;
	scanf("\n", input);
	
	for (int t = 1; t <= T; t++) {
		//input
		fgets(input, 1100, stdin);
		inp = input;
		
		ta=n=0;
		sscanf(inp, "%d%n", &smax, &pos);
		inp += pos;
		inp++;
		
		for (int i=0; i <= smax; i++) {
			sscanf(inp, "%1d", &slevel);
			inp++;
			
			if (slevel > 0) {
				if (ta >= i) {
					ta += slevel;
				} else {
					n += (i - ta);
					ta += slevel + (i - ta);
				}
			}
			//cout << slevel << " ";
		}
		
		cout << "Case #" << t << ": " << n << endl;
	}
	
	return 0;
}












