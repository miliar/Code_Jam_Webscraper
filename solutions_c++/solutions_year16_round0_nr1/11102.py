//
//  problem1.cpp
//  
//
//  Created by Elahe Farjami on 4/9/16.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int problem1Process(const int n) {
	if(n == 0) {
		return -1;
	}
	int digitCounter=0;
	int digits[10];
	for(int i=0; i<10; i++) {
		digits[i] = 0;//not seen
	}
	//cout<<"current n: " << n << endl;
	for(int i=1; i<1000000; i++) {
		int m=i*n;
		int changing_m = m;
		//cout<<"current m: " << m << endl;
		//find digits of m, and cross corresponding digits, and increment counter
		while(changing_m>0) {
			int d = changing_m%10;
			if(digits[d] == 0) {
				digits[d] = 1;
				digitCounter++;
				if(digitCounter == 10) {
					return m;
				}
			}
			changing_m/=10;
		}
	}
	return -1;
}

void problem1() {
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");

	int T;
	infile >> T;

	for(int i=0; i<T; i++) {
		int N;
		infile >> N;
		//if res=-1, insomnia
		int res = problem1Process(N);
		outfile << "Case #" << i+1 << ": ";
		if(res == -1) {
			outfile << "INSOMNIA\n";
		}
		else if(res >= 0) {
			outfile << res << "\n";
		}
		else {
			cout<<"Error occured\n\n\n";
		}
	}
}


int main() {
    
    cout<<"Start problem1\n";
    problem1();
    cout<<"Finish problem1\n";

    
    return 0;
    

}