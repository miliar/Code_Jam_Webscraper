#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <bitset>
#include <cstdlib>

using namespace std;
int main(int argc, char* argv[]) {

	int t;
	int n;
	int j;
	cin >> t;

	cin >> n;
	cin >> j;

	int jam[n] = {0};
	jam[0] = 1;
	jam[n-1] = 1;

	bool flag = true;
	int counter = 0;


	long long int divv[9] = {0};
	for (int e = 1; e <= t; e++) {

		cout << "Case #" << e << ":" << endl; 
		
		while (counter < j) { 
			
			/*cout << "gen num:";
			for (int oo = 0; oo < n ; oo++)
				cout << jam[oo];
			cout << endl;*/
			int countNum = 0;
			for (int jj = 2; jj < 11; jj++) {
				 long long int num = 0;

				for (int kk = n-1; kk > -1; kk--) {
					if (jam[kk] == 1) 
						num = num + pow(jj, n - 1 - kk);
				}
			//	if (jj == 5)
			//		cout << num;
				for (int ii=2; ii < sqrt(num); ii++) {
					if (num % ii == 0) {
						divv[jj-2] = ii;
						countNum = countNum + 1;
						break;

					}
				}
				
			}
			if (countNum == 9)
			{
				for (int oo = 0; oo < n ; oo++)
					cout << jam[oo];
				for (int k=0; k <9;k++)
					cout << " " << divv[k];
				cout << endl;
				counter = counter + 1;
			}

			jam[n-2] = jam[n-2] + 1;
			for (int p=n-2;p>0;p--) {
				if (jam[p] == 2){
					jam[p-1]++;
					jam[p] = 0;
				}
				else {
					break;
				}
			}

			
		}
	}


}