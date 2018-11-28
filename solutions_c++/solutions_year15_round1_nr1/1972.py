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
		
		int t = 0, c = 1, num_inputs = 0;
		inputFile>>t;
		
		
		while(c <= t) {
			inputFile>>num_inputs;
			int x = 0;
			int min_sum_1 = 0;
			int min_sum_2 = 0;
			int rate = 0;
			int a[1000] = {0};
			
			while(x < num_inputs) {
				inputFile>>a[x];
				x++;
			}
			
			for(x = 0; x < num_inputs - 1; x++) {
				if(a[x] > a[x+1]) {
					min_sum_1 += a[x] - a[x+1];
				}
			}
			
			for(x = 0; x < num_inputs - 1; x++) {
				//Find the rate at which she eats
				cout<<a[x]<<" "<<a[x+1]<<endl;
				if(a[x] > a[x+1]) {
					if((a[x] - a[x+1]) > rate) {
						rate = a[x] - a[x+1];
					}
				}
			}
			
			
			
			if(rate > 0) {
				for(x = 0; x < num_inputs - 1; x++) {
					if(a[x] > rate) {
						min_sum_2 += rate;
					} else {
						min_sum_2 += a[x];
					}
				}
			} else {
				min_sum_2 = 0;
			}
			
			outputFile<<"Case #"<<c<<": "<<min_sum_1<<" "<<min_sum_2<<"\n";
			c++;
		}
		outputFile.close();
	} else {
		cout<<"Could not open the file";
	}
	
	inputFile.close();
	return 0;
}