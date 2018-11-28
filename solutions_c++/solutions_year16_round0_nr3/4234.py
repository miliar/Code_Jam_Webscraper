#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <bitset>
#include <climits>
using namespace std;

unsigned long long basen(bitset<16> number,unsigned long long &base) {
	unsigned long long three = 0;
	int j=0;
	while(j<16) {
		auto rem = number[j];
		three = three + rem*pow(base,j);
		j++;
	}
	return three;
}

unsigned long long isPrime(unsigned long long number) {
	for(unsigned long long i=2;i<=sqrt(number);i++) {
		if(number%i==0) {
			return i;
		}
	}
	return -1;
}
int main() {
	unsigned long long ii = 0b1111111111111111;
	unsigned long long arr[9] = {0};
	unsigned long long divi[9] = {0};
	cout<<"Case #1:"<<endl;
	int j =0;
	while(ii>pow(2,15) && j!=50) {
		int flag = 0;
		std::bitset<16> im3(ii);
		//cout<<im3<<" ";		
		for(unsigned long long i=2;i<11;i++) {
			arr[i-2] = basen(im3,i);
			//cout<<arr[i-2]<<" ";
		}
		for(int i=2;i<11;i++) {
			divi[i-2]= isPrime(arr[i-2]);
			//cout<<divi[i-2]<<" ";
		}
		//cout<<endl;
		for(int i=2;i<11;i++) {
			if(divi[i-2] == ULLONG_MAX) {
				flag = 1;
				break;
			}
		}
		if(flag==0) {
			++j;
			cout<<" "<<im3;
			for(int i=2;i<11;i++) {
				cout<<" "<<divi[i-2];
			}
			cout<<endl;
		}
		ii = ii-2;
	}
}