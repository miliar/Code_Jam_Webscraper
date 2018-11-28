#include <iostream>
#include <cmath>
using namespace std;

unsigned int seived[100000001] = {0};
int divisors[11];

unsigned long long trial_divs[100000000];

int main (){
	cout << "Case #1:" << endl;
	int ncases;
	cin >> ncases;
	int n,j;
	cin >> n >> j;
	unsigned long long upper_lim = ceil(sqrt(pow(10,n)));	
	unsigned long long seive_lim = ceil(sqrt(ceil(sqrt(pow(10,n)))));
	int ntdivs = 0;
	for(unsigned long long i = 2; i < seive_lim; i++){
		if(seived[i] == 0){
			trial_divs[ntdivs++] = i;
			for(unsigned long long j = i*i; j < upper_lim; j += i){
				seived[j] = i;
			}
		}
	}
	int count = 0;
	int start = (1 << (n-1));
	int end = (1 << n);
	for(int i = start; i < end; i++){
		if(count >= j) break;
		if(!bool(i & 1)) continue;
		bool works = true;
		for(int base = 2; base <= 10; base++){
			unsigned long long result = 0;
			for(int j = 0; j < n; j++){
				bool digit = i & (1 << j);
				if(digit) result += pow(base,j);
			}
			//cout << "Base: " << base << " number as " <<  result << endl;
			int prime = true;
			for(int j = 0; j < ntdivs; j++){
				if(result % trial_divs[j] == 0){
					//cout << "divides evenly by " << trial_divs[j] << endl;
					prime = false;
					divisors[base] = trial_divs[j];
					break;
				}
			}
			if(prime){
				//cout << "result is prime" << endl;
				works = false;
				break;
			}
		}
		if(works){
			count+= 1;
			for(int j = n-1; j >= 0; j--){
				cout << bool(i & (1 << j));
			
			}
			for(int j = 2; j <= 10; j++){
				cout << " " << divisors[j];
			}
			cout << endl;
		}
	}

	return 0;
}


