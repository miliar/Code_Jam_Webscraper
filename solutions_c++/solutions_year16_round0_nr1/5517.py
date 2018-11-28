//============================================================================
// Name        : codejam-A.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

long long inf = 1000000000000000000;
int check[15];

int main() {
	int test;
	long long n;
	cin >> test;
	for(int t = 1; t <= test; t++){
		cin >> n;
		if(n == 0){
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else {
			for(int i = 0; i < 10; i++) check[i] = 0;
			int newnum = 0;
			long long tmpn;
			long long muln = n;
			while(muln < inf) {
				tmpn = muln;
				while(tmpn > 0) {
					int digit = tmpn % 10;
					if(check[digit] == 0){
						newnum++;
						if(newnum == 10){
							cout << "Case #" << t << ": " << muln << endl;
							break;
						}
					}
					check[digit] = 1;
					tmpn /= 10;
				}
				if(newnum == 10) break;
				muln += n;
			}
		}
	}
	return 0;
}
