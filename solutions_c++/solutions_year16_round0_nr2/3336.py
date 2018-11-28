#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);

	for (int i = 0; i < t; i++){
		string s;
		cin >> s;
		char prev = '+';
		int steps = 0;
		for (int j = s.length()-1; j >=0; j--){
			if (s[j] != prev){
				steps++;
			}
			prev = s[j];
		}
		printf("Case #%d: %d\n",i+1,steps);
	}
}