#include <iostream>
#include <cmath>
using namespace std;
long readAsBase(long x, long base){
	long ret = 0;
	int digits = 0;
	while(x != 0){
		
		if(x % 2 == 1){
			ret += pow(base, digits);
		}
		x /= 2;
		digits++;
	}
	return ret;
}
long toBinary(long x, long base){
	long ret = 0;
	int digits = 0;
	while(x != 0){
		ret = ret * 10 + x % base;
		x /= base;
		digits++;
	}
	long out = 0;
	for(int i = 0; i < digits; i++){
		out = out * 10 + ret % 10;
		ret /= 10;
	}
	return out;
}
long findDivisor(long x){
	for(long i = 2; i <= sqrt(x); i++){
		if(x % i == 0){
			return i;
		}
	}
	return -1;
}
long testfindDivisor(){
	cout << findDivisor(5) << endl;
	cout << findDivisor(32) << endl;
	cout << findDivisor(51) << endl;
	cout << findDivisor(49) << endl;
	cout << findDivisor(53) << endl;
}
int main(int argc, char ** argv){
	long t, n, c;
	cin >> t >> n >> c;
	cout << "Case #1:" << endl;
	//testfindDivisor();
	long val;
	long list[9];
	long found = 0;
	for(long i =32769; i < 65535; i+=2){
	//for(long i =33; i < 64; i+=2){
		//cerr << "Trying " << toBinary(i,2) << endl;
		bool isCoin = true;
		for(long j = 2; j < 11; j++){
			//cerr << readAsBase(i,j) << endl;
			val = findDivisor(readAsBase(i, j));
			if(val == -1){
				isCoin = false;
				break;
			} else {
				list[j-2] = val;
			}
		}
		if(isCoin){
			cout << toBinary(i,2);
			for(long k = 0; k < 9; k++){
				cout << " " << list[k];
			}
			cout << endl;
			found++;
			if(found == c){
				break;
			}
		}
	}
	return 0;
}
