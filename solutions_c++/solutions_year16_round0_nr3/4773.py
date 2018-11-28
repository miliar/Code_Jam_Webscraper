#include <set>
#include <iostream>

using namespace std;

long long change(long long number, long long base){
	long long i = 0;
	long long baseTmp = 1;
	long long result = 0;
	while(number){
		if(number % 2L == 1){
			result += baseTmp;
		}
		baseTmp *= base;
		i++;
		number >>= 1;
	}
	return result;
}

long long findDivisor(long long a, long long start, long long base){
	for(long long i = start; (long long)(i * i) <= (long long)a; i++){
		if( (a / i) * i == a){
			return i;
		}
	}

	return 0L;
}

string longLong2Bin(long long a){
	string result = "";
	while(a){
		result = (a&1 ? "1":"0") + result;
		a >>= 1;
	}
	return result;
}


int main(){
	long long t;
	cin >> t;
	long long n, j;
	long long divisors[20];
	bool good;

	cin >> n >> j;

	cout << "Case #1:" <<endl;

	long long count = 0;
	long long changed;

	for(long long i = (1<<(n - 1)); count < j; i++){
		good = true;

		for(long long j = 2; j <= 10; j++){
			changed = change(i, j);
			divisors[j - 2] = findDivisor(changed, j, 2);
			if(divisors[j - 2] == 0)
				good = false;
		}
		if(good && (i & 1)){
			cout << longLong2Bin(i);
			for(long long j = 2; j <= 10; j++){
				cout << " " << divisors[j - 2];
			}
			cout << endl;
			count++;
		}
	}
	return 0;
}