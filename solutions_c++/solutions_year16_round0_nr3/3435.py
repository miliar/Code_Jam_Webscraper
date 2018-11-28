#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>


using namespace std;

long isPrime(long num) {

        for(int i = 2; i <= sqrt(num); i += 2)
        {
                if(i % 2 == 0)
                        i++;

                if((num % i) == 0)
                {
                        return i;
                }
        }

        return -1;
}


int main() {
	int test;
	cin >> test;
	int n;
	for (n = 0; n < test; n++) {
		cout<<"Case #"<<(n + 1)<<":"<<endl;;
		int length;
		int printnum;
		cin >>length;
		cin >>printnum;
		int t;
		int ql;
		t = pow(2, length- 1) + 1;
		ql = pow(2, length);
		int z;
		string binarystring;
		int count = 0;;
		for (z = t; z < ql; z = z+2) {
			int p;
			int tmp = z;
			while (tmp != 0) {
				p = tmp % 2;
				tmp = tmp / 2;
				binarystring = binarystring + to_string(p);
			}

			long array[9] = {-1};
			int size = binarystring.length();
			int j;
			int i;
			bool notprime = true;
			for (i = 2; i < 11; i++) {
				long k = 0;
				for (j = 0; j < size; j++) {
					char d = binarystring.at(j);
					if (d == '1') {
						k = k + pow(i, size - j - 1);
					}
				}
				//cout<<k<<endl;
				if (isPrime(k) == -1) {
					notprime = false;
					break;
				} else {
					array[i - 2] = isPrime(k);
				}
			}
			//cout<<count<<endl;
			if (notprime != false) {
				count++;
				cout<<binarystring<<" ";
				for (i = 0; i < 9; i++) {
					cout<<array[i]<<" ";
				}
				cout<<endl;
			}

			binarystring = "";
			if (count == printnum) {
				break;
			}
		}

	}
}