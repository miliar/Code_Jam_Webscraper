#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int digits(unsigned long long a){
	return floor(log10(a))+1;
}

bool is_end_ok(int *a){
	for(int i = 0;i < 10;i++){
		if(a[i] == 0){
			return false;
		}
	}
	return true;
}

int num_of_digit(unsigned long long a, int b){
	return int(floor(a/pow(10, b)))%10;
}
	

int main(void){
	unsigned long long a;
	unsigned long long n;
	cin >> n;
	for(unsigned long long i = 0;i < n;i++){
		int f[10] = {0};
		int d;
		cin >> a;
		if(a == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		for(int j = 0;j < 100;j++){
			if(is_end_ok(f)) break;
			d = a*(j+1);
			for(int k = 0;k < digits(d);k++){
				f[num_of_digit(d, k)] = 1;
			}
		}
		cout << "Case #" << i+1 << ": " << d << endl;
	}
	return 0;
}

