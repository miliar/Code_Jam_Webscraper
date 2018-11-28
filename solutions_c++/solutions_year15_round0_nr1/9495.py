#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	short T;
	short Si, i;
	string S;
	short invitados, ovacionando, verguenza;
	string::iterator sIt, end;

	cin >> T;
	for (short j = 1; j <= T; ++j) {
		invitados = 0, ovacionando = 0, i = 0;
		cin >> verguenza >> S;
		for (sIt = S.begin(), end = S.end(); sIt != end; sIt++) {
			Si = *sIt - 48;

			if (Si != 0) {
				if (ovacionando + invitados < i) {
					invitados = i - ovacionando;	
				}	
			}
			ovacionando += Si;
			
			if (ovacionando >= verguenza)
				break;

			i++;
		}
		cout << "Case #" << j << ": " << invitados << endl;		
	}	
	return 0;
}
