#include <bits/stdc++.h>

using namespace std;

bool isPrime(unsigned long long num){
	unsigned long long root = (unsigned long long) pow(num,0.5);
	for(unsigned long long i = 2; i <= root ; i ++){
		if(num % i == 0){
			return false;
		}
	}
	return true;
}

unsigned long long firstDivisor(unsigned long long num){
	unsigned long long root = (unsigned long long) pow(num,0.5);
	for(unsigned long long i = 2; i <= root ; i ++){
		if(num % i == 0){
			return i;
		}
	}
	return num;
}

unsigned long long toBaseTen(unsigned long long num, int base){
	unsigned long long converted = 0;
	int count = 0;
	while(num != 0){
		unsigned long long digit = num % 10;
		if(digit == 1){
			converted += ((unsigned long long)pow(base,count))*digit;
		}
		count ++;
		num = num/10;
	}
	return converted;
}

unsigned long long makeNumber(unsigned long long num, int n){
	unsigned long long converted = 1;
	int count = 1;
	while(num != 0){
		unsigned long long digit = num % 2;
		if(digit == 1){
			converted += ((unsigned long long)pow(10,count))*digit;
		}
		count ++;
		num = num/2;
	}
	converted += ((unsigned long long)pow(10,n-1));
	return converted;
}

int main(){

	int t , n , j;
	cin >> t;
	for(int s = 1; s <= t ; s++){
		cin >> n;
		cin >> j;
		vector<unsigned long long> jamcoin(j,0);
		unsigned long long val = 0;
		int count = 0;
		while( count < j ){
			unsigned long long trail_num = makeNumber(val,n);
			val++ ;
			bool valid = true;
			for(int i = 2 ; i < 11 ; i++){
				unsigned long long converted = toBaseTen(trail_num, i);
				if(isPrime(converted)){
					valid = false;
					break;
				}
			}
			if(valid){
				jamcoin[count] = trail_num;
				count++;
			}
			
		}
		cout<<"Case #"<<s<<":"<<endl;
		for(int i = 0; i < j; i++){
			cout << jamcoin[i]<<" ";
			for(int k = 2 ; k < 11 ; k++){
				unsigned long long converted = toBaseTen(jamcoin[i], k);
				cout << firstDivisor(converted)<<" ";
			}
			cout <<endl;
		}
		
	}
	return 0;
}