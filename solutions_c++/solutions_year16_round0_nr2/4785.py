#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;


int main() {
	int t, c, n, i, j;
	char input[101];
	string aux;

	scanf("%d", &t);
	c = 1;
	while (t--) {
		scanf("%s", input);
		aux = string(input);
		n = 0;
		while (true) {
			if (aux[0] == '-') {
				i = 0;
				while (aux[i + 1] == '-') 
					i++;
				while (i >= 0) {
					aux[i] = '+';
					i--;
				}
			} else {
				i = 0;
				while (aux[i + 1] == '+')
					i++;
				if (i == aux.size() - 1) {
					cout << "Case #" << c << ": " << n << endl;
					c++;
					break;
				}
				while (i >= 0) {
					aux[i] = '-';
					i--;
				}
			}
			n++;
		}
	}


	return 0;

}
