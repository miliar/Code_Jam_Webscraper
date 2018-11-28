//============================================================================
// Name        : codejam-B.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	int test;
	string pancake;
	cin >> test;
	for(int t = 1; t <= test; t++){
		cin >> pancake;

		int count = 0;
		int lastidx = pancake.length();
		while(lastidx >= 0){
			for(int i = pancake.length()-1; i >= 0; i--){
				if(pancake[i] == '-') break;
				lastidx = i-1;
			}
			if(lastidx < 0) break;
			count++;
			if(pancake[0] == '+') {
				for(int i = 0; i < pancake.length(); i++){
					if(pancake[i] == '-') break;
					pancake[i] = '-';
				}
			}
			else{
				string toppan = pancake.substr(0, lastidx+1);
				int i, j;
				for(i = 0, j = lastidx; j >= 0; i++, j--) {
					if(toppan[j] == '+') pancake[i] = '-';
					else pancake[i] = '+';
				}
			}
//			cout << pancake << endl;
		}
		cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}
