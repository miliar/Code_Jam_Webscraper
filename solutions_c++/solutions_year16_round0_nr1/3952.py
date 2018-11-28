#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;


int main() {
	int test;
	cin >> test;

	bool* a;
	a = (bool*) malloc(10 * sizeof(bool));

	int n;
	for (n = 0; n < test; n++) {
		int N;
		cin >> N;
		cout<<"Case #"<<(n + 1)<<": ";
		int i;
		int remain = 10;
		for (i = 0; i < 10; i++) {
			a[i] = false;
		}
		int p = 1;
		int q;
		while (remain > 0) {
			q = p * N;
			do {
    			int digit = q % 10;
    			if (a[digit] == false) {
    				a[digit] = true;
    				remain--;
    			} else {
    				a[digit] = true;
    			}
    			q /= 10;
			} while (q > 0);


			p++;

			if (p == 1000000) {
				cout<<"INSOMNIA"<<endl;
				break;
			}
		}


		if (p != 1000000) {
			cout<<(p - 1) * N <<endl;
		}

	}



}

