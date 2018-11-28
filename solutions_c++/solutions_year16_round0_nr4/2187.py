#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <bitset>
#include <cstdlib>

using namespace std;
int main()
{
	int t,k,c,s;
	cin >> t;

	

	

	for (int i = 1; i <= t ; i++) {
		cin >> k;
		cin >> c;
		cin >> s;
		cout << "Case #" << i << ": " << 1;

		for (int l = 2; l <= s; l++) {

			long long int ind = l;
			for (int p = 1; p <= c-1;p++)
				ind = (ind - 1) * k + l;
			cout << " " << ind;
		}

		cout << endl;



		 
	}
}