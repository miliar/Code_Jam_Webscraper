#include<iostream>
#include<math.h>
#include <fstream>
using namespace std;
long long int w;
inline bool getBit(unsigned short int byte, int position){
	return (byte >> position) & 0x1;
}
int isnotprime(){
	long long int i;
	for (i = 2; i*i <= w; i++){
		if (w%i == 0){
			return i;
		}
	}
	return 0;
}
long long int tobase(unsigned short int n, long long int b){
	long long int i, p = 1;
	long long int ans = 0;
	for (i = 0; i < 16; i++, p *= b){
		ans += getBit(n, i)*p;
	}
	return ans;
}
int main(){
	ifstream cin("C-small-attempt3.in");
	ofstream cout("output.out");
	long long int i, t, n, j, o = 0;
	long long int list[9];
	bool sw;
	unsigned short int number = 32769;
	cin >> t;
	while (t--){
		cin >> n >> j;
		o++;
		cout << "Case #" << o << ":" << endl;
		while (j){
			sw = 0;
			if (getBit(number, 0) == 1){
				w = number;
				if (list[0] = isnotprime()){
					sw = 1;
					for (i = 3; i <= 10; i++){
						w = tobase(number, i);
						list[i - 2] = isnotprime();
						if (list[i - 2] == 0){
							sw = 0;
							break;
						}
					}
				}
			}
			if (sw == 1){
				for (i = 15; i >= 0; i--){
					cout << getBit(number, i);
				}
				for (i = 0; i < 9; i++){
					cout << " " << list[i];
				}
				cout << endl;
				j--;

			}
			number++;
		}
	}
	return 0;
}