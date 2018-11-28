#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
	fstream inputFile;
	inputFile.open("A2.in.txt", ios::in);
	
	if(inputFile.is_open()) {
		ofstream outputFile;
		outputFile.open("output2.txt");
		
		int t = 0;
		inputFile>>t;
		
		int c = 1;
		while(c <= t) {
			int sum = 0;
			int count = 0;
			char s[1100];
			int characters = 0;
			inputFile>>characters;
			inputFile>>s;
			
			sum += s[0] - '0';
			for(int i = 1; i <= characters; i++) {
				if(s[i] > 0) {
					while(sum < i) {
						count++;
						sum++;
					}
				}
				sum += s[i] - '0';
			}
			outputFile<<"Case #"<<c<<": "<<count<<"\n";
			c++;
		}
		outputFile.close();
	}
	inputFile.close();
	return 0;
}