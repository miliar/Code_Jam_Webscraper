
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;


int main() {

	int T,I=1;
	cin >> T;
	int N,L,A,B,K,acoes,i,j;
	while (T--) {

		cin >> N;

		std::string *s = new std::string[N];

		for(i=0;i<N;i++)
			cin >> s[i];

		acoes = 0;
		i=j=0;
		bool impossible = false;
		while(1) {
			if (i==s[0].size() || j==s[1].size()){
				if (i==s[0].size()) {
					if (j==s[1].size()) break;
					else if (s[1][j] == s[1][j-1]) {
						acoes++; j++; continue;
					} else {
						impossible = true;
						break;
					}
				} else {
					if (s[0][i] == s[0][i-1]) {
						acoes++; i++; continue;
					} else {
						impossible = true;
						break;
					}
				}
			}
			if (s[0][i] == s[1][j]) {
				i++; j++;
				continue;
			} else {
				if (i==0){
					impossible = true;
					break;
				}
				if (s[0][i] == s[0][i-1]) {
					acoes ++;
					i++;
					continue;
				}
				if (s[1][j] == s[1][j-1]) {
					acoes ++;
					j++;
					continue;
				}
				impossible = true;
				break;
			}
		}

		cout << "Case #" << I << ": ";
		if (impossible) cout << "Fegla Won";
		else cout << acoes;
		cout << endl;
		I++;
	}
	return 0;
}
