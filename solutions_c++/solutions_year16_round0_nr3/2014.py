#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

int factor[10];



int main (){
	long long maxnum;
	for (int p=0; p<=30; p++){
	maxnum += 1<<p;
	}
	ofstream myfile;
 	myfile.open ("ofile.txt");
	int found = 0;
	myfile << "Case #1:" << endl;
	for (unsigned long long start = (1<<30); start <= maxnum; start ++){
		if (found == 500){
			break;
		}
		int digits [32];
		long long  copy = start;
		for (int i=30; i>=0; i--){
			digits[i] = copy%2;
			copy = copy >> 1;
		}
		digits [31] = 1;
		for (int i=0; i<=31; i++){
			cout << digits[i];
		}
		int possible = 1;
		int actual = start*2 + 1;
		for (int base =2 ; base<=10; base++){
			int prime = 1;
			long long end = 10000;
			for (long long test =2 ; test <=end; test= test+2){
				if (test == 2){
					int mod = 0;
					for (int i=0; i<=31; i++){
						mod = (mod*base + digits[i])%2;
					}
					if (mod == 0){
						factor[base] = 2;
						prime = 0;
						break;
					}
					else {
						test = test +1;
					}
				}
				else {
					int mod = 0;
					for (int i=0; i<=31; i++){
						mod = (mod*base + digits[i])%test;
					}
					if (mod ==0){
						factor[base] = test;
						prime = 0;
						break;
					}
				}	
			}
			if (prime == 1){
				possible = 0;
				break;
			}
		}
		if (possible){
			found ++;
			cout << " FOUND";
			for (int k=0; k<=31; k++){
				myfile << digits[k];
			}	
			for (int k=2; k<=10; k++){
				myfile << " " << factor[k];
			}
			myfile << endl;
			}
		cout << endl;
	}
	myfile.close();
	
}
