#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>

using namespace std;

int min(int x, int y) {
	return x < y ? x : y;
}
int max(int x, int y) {
	return x > y ? x : y;
}

int main(int argc, char *argv[]) {
	fstream inputFile;
	inputFile.open("D1.in.txt", ios::in);
	
	if(inputFile.is_open()) {
		ofstream outputFile;
		outputFile.open("outputD1.txt");
		int t = 0;
		inputFile>>t;
		int count = 1;
		string win;
		
		while(t--) {
			int x, r, c;
			inputFile>>x>>r>>c;
			
			switch(x) {
				case 1:
					win = "GABRIEL";
					break;
				case 2:
					if(r % 2 == 0 || c % 2 == 0) {
						win = "GABRIEL";
					}
					else {
						win = "RICHARD";
					}
					break;
				case 3:
					if(r < 3 || c < 3) {
						if((min(r,c) == 2 && max(r,c) == 3) || (min(r,c) == 3 && max(r,c) == 4)) {
							win = "GABRIEL";
						} else {
							win = "RICHARD";
						}
					} else if(r == 4 && c == 4) {
						win = "RICHARD";
					} else {
						win = "GABRIEL";
					}
					break;
				case 4:
					if(r == 4 && c == 4) {
						win = "GABRIEL";
					} else if(min(r, c) == 3 && max(r, c) == 4) {
						win = "GABRIEL";
					} else {
						win = "RICHARD";
					}
					break;
			}	
			
			outputFile<<"Case #"<<count<<": "<<win<<"\n";
			count++;
		}
		
	}
	return 0;
}