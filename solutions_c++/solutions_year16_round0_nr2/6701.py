#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
int main() {
	int cc;
	cin >> cc;
	for(int i=0 ;i<cc; i++) {
		printf("Case #%d: ",i+1);
		string s;
		cin>>s ;
		char type = s[0];
		int c=0;
		for(int i=1; i<s.size(); i++) {
			if(type != s[i]) {
				c++;
				for(int j=0; j<i; j++) {
					s[i] = 88-type;
					// '+' : 43, '-' : 45
				}
				type=88-type;
			}
		}
		if(type == '-') c++;
		printf("%d\n",c);
	}
}
