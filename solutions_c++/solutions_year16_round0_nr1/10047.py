#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>

using namespace std;

int main(){
	int i, j, k;
	int bit;
	int n, t;
	cin >> t;

	for (i = 1; i <= t; i++){
		cin >> n;
		cout << "Case #" << i << ": ";
		bit = 0;
		for (j = 1;j<=10000; j++){
			k = n*j;
			for (; k != 0; k /= 10){
				bit |= 1 << (k % 10);
			}
			if (bit == 1023){
				cout << n*j << endl;
				goto loop;
			}
		}
		cout << "INSOMNIA" << endl;
	loop:
		;
	}
	return 0;
}