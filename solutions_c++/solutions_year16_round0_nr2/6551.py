#include <iostream>
#include <string>
using namespace std;

void shift (char * p, int j) {
        while (j >=0) {
                if (p[j] == '+') {
                        p[j] = '-';
                }
                else {
                        p[j] = '+';
                }
                j--;
        }
}



int main () {

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		char * pan = new char [100];
		cin >> pan;
		int len = 0;
		while (pan [len] != '\0') {
			len++;
		}
		int count = 0;
		for (int j = len - 1; j >= 0; j--) {
			if (pan [j] == '+') {
				continue;
			}
			else {
				shift (pan, j);
				count++;
			}
		}
		cout << "Case #" << i << ": " << count << " " << endl;
	}
}

