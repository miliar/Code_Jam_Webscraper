#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <stdio.h>

using namespace std;

int main(){
	
	int t;
	cin >> t;;
		
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		if (n == 0)
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else {
			int tabla = 0;
			for (int j = 1; tabla != 1023 ; j++) {
				int r = n * j;
				
				for (int aux = r;aux > 0; aux = aux / 10)
					tabla = tabla | (1 << (aux % 10));
				//cout << r << " " << tabla << endl;
				if (tabla == 1023)
					cout << "Case #" << i + 1 << ": " << r << endl;
				
			}
		}
	}
	
	return 0;
}
