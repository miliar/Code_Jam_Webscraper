#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>

using namespace std;
int main (int argc, char * const argv[]) {
    int cases, buffer, run, method1, method2, fome;
	cin >> cases;
	
	int pics;
	int plate[1002];
	
	for (buffer = 0; buffer < cases; buffer++) {
		cout << "Case #" << buffer + 1 << ": ";
		
		cin >> pics;
		for (run = 0; run < pics; run++) {
			cin >> plate[run];
		}
		
		method1 = 0;
		method2 = 0;
		fome = 0;
		
		for (run = 0; run < pics - 1; run++) {
			if (plate[run + 1] < plate[run]) {
				method1 = method1 - plate[run + 1] + plate[run];
				if (plate[run] - plate[run + 1] > fome) {
					fome = plate[run] - plate[run + 1];
				}
			}
		}
		
		for (run = 0; run < pics - 1; run++) {
			method2 = method2 + min(fome, plate[run]);
		}
		
		cout << method1 << " " << method2 << endl;		
	}
	
	return 0;
}
