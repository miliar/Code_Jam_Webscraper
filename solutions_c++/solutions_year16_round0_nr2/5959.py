#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int T;
	string in;
	
	scanf("%d", &T);
	getchar();
	
	for (int i = 1; i <= T; i++) {
		getline(cin, in);
		
		int steps = 0;
		
		while(1) {
			size_t foundF = in.find_first_of('-');
			
			if (foundF == string::npos) { break; }
			
			size_t foundL = in.find_last_of('-');
			in = in.substr(0, foundL+1);
			
			if (foundF != foundL) {
				if (in[0] == '+') {
					in[0] = '-';
					int j = 1;
					while (in[j] == '+') {
						in[j] = '-';
						j++;
					}
					steps++;
				}
			} else {
				in.erase( in.end()-1 );
			}
			
			string newIn = "";
			for (int j = 0; j < in.size(); j++) {
				newIn = ( in[j] == '-' ? '+' : '-' ) + newIn;
			}
			in = newIn;
			steps++;
		}
		
		printf("Case #%d: %d\n", i, steps);
	}
	
	return 0;
}
