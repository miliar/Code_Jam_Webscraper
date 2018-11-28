#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int nn;
	scanf("%d\n", &nn);
	for(int cc=1; cc<=nn; cc++) {
		printf("Case #%d: ", cc);
		
		string s;
		getline(cin, s);
		
		int c = 0;
		for(int i=0; i<s.length()-1; i++) {
			if(s[i] != s[i+1]) {
				c++;
			}
		}
		
		if(s[s.length()-1] == '-') {
			c++;
		}
		
		printf("%d\n", c);
	}
	
	return 0;
}
