#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

long long isnotPrime (long long n){
	if(n <= 3) return n;
	if(n % 2 == 0) return 2;
	if(n % 3 == 0) return 3;
	for(long long i = 2;i * i <= n;i ++){
		if(n % i == 0) return i;
	}
	return 0;
}

bool isJamCoin (int x[], int n){
	long long base[11];
	long long factor[11];
	memset(base, 0, 88);
	for(int i = 0;i < n;i ++){
		for(int j = 2;j < 11;j ++){
			base[j] = (base[j] * j) + x[i];
		}
	}
	for(int j = 2;j < 11;j ++){
		factor[j] = isnotPrime(base[j]);
		if(!factor[j]) return false;
	}
	
	cout << base[10] << " ";
	for(int j = 2;j < 11;j ++){
		cout << factor[j] << " ";
	}
}

int main(){
	int T;
	cin >> T;
	int n, J;
	cin >> n >> J;
	int x[32];
	memset(x, 0, 128);
	
	x[0] = 1;
	x[n - 1] = 1;
	
	int count = 0;
	cout << "Case #1:" << endl;
	while(count < J){
		int i;
		for(i = n - 2;i >= 0;i --){
			if(x[i] == 0) break;
		}
		x[i] = 1;
		for(int j = i + 1;j < n - 1;j ++){
			x[j] = 0;
		}
		if(isJamCoin(x, n)){
			count ++;
			cout << endl;
		}
	}
	
	return 0;
}
