#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <bitset>
#include <cstdlib>

using namespace std;
int main() {

	int t;
	cin >> t;

	int counter = 1;
	while (counter <= t) {
		cout << "Case #" << counter << ": ";
		long long int n;
		cin >> n;
		bool nums[10] = {false};

		bool flag = false;
		if (n == 0)
			cout << "INSOMNIA" << endl;
		else {
			int a = 1;
			long long int mm = n;
			do {
				
				n = mm * a;
				long long int m = n;
				do {
		    		long long int digit = m % 10;
		    		nums[digit] = true;
		    		m /= 10;
				} while (m > 0);

				
				flag = true;
				for (int i =0; i < 10; i++)
				{
					if (nums[i] == false)
					{
						flag = false;
						break;
					}
				}
				a = a + 1;
				

			}while (flag ==false);
			cout << n << endl;
		}
		counter = counter + 1;
	}


}