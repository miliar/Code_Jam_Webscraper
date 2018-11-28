#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char data_count[256];
char cn[64];

int
main(int argc, char** argv)
{
	int N, a, n=1;
	cin >> N;
	while(n <= N) {
		memset(data_count, 0, 256);
		cout << "Case #" << n << ": ";
		cin >> a;
		if (a == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			bool done = false;
			int mult = 2;
			int a_orig = a;
			while(!done) { 
				sprintf(cn, "%d", a);
				int i = 0;
				while(cn[i]) {
					data_count[cn[i]]++;
					i++;
				}
				done = true;
				for (char c = '0'; c <= '9'; c++) {
					if (data_count[c] == 0) {
						done = false;
						break;
					}
				}
				if (!done) {
					a = a_orig * mult;
					mult++;
				}
			}
			cout << a << endl;	
		}
		n++;
	} 
	return 0;
}