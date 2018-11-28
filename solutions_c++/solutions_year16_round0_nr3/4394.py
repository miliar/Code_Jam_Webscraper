#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
using namespace std;
unsigned long long power(unsigned long long num, unsigned long long po){
	unsigned long long result = 1;
	for (unsigned long long i=0;i<po;i++){
		result = result*num;
	}
	return result;
}
unsigned long long isPrime(unsigned long long value){
		
	for (unsigned long long i=2;i<value;i++){
			// cout << i << endl;

		if (value%i ==0){
			return i;
		}
		if(i > 100000){
			// cout << value << "in prime\n";
			return 0;
		}
	}
	// cout << value << "in prime\n";
	return 0;
}
unsigned long long convertTo(int numbers[], int base,int length){
	unsigned long long sum =0;
	// int num = number;
	// cout << "convert in\n";
	for (int i=0;i<length;i++){

		sum = sum + (numbers[length-(i+1)])*power(base, i);
		// num = num/10;
	}
	return sum;
}
int main(){
	int num_test_cases;
	int jam_length, num_outputs;
	FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
    assert(fin!=NULL);
    FILE *fout = freopen("C-small-attempt0.out", "w", stdout);
	cin >> num_test_cases;
	cin >> jam_length >> num_outputs;
	// cout << num_outputs;
	cout << "Case #1:" << endl;
	// vector<int> numbers[jam_length];
	int numbers[jam_length];
	vector<int> divisors;
	int index =0;
	for (unsigned long long j=0;j<power(2,jam_length-2);j++){
	int valcount = 0;
	// vector<unsigned long long> stored_val;
		unsigned long long stored_val[9];
	// cout << "for in inner numbers\n";
		
		int x = j;
		for (int k=0;k<jam_length-2;k++){
			// cout << "for in decimal to binary\n";
			numbers[jam_length-2-k] = x%2;
			x=x/2;
		}
		numbers[0] =1;
		numbers[jam_length-1] = 1;
		// for (int i = 0; i < jam_length; i++)
		// {
		// 	cout << numbers[i] < " ";
		// }
		// cout << endl;
		for (int i=2;i<=10;i++){
			// cout << "storing dofferent base val\n";
		stored_val[valcount] = convertTo(numbers, i, jam_length);
		// cout << stored_val[valcount] << " ";
		valcount++;
		}
		// cout << endl;
		bool check = false;
		for (int i=0;i<9;i++)
		{
			 // check = true;
			 // cout << "asdasdasd\n";
			if (isPrime(stored_val[i]) == 0){
				check = false;
				break;
			}
			else{
				check = true;
			}
		}
		if (check == true){
			// cout << "yahan\n";
			index++;
			// cout << index << endl;
			for (int j=0;j<jam_length;j++){
					cout << numbers[j];
				}
				cout << " " ;
			for (int i=0;i<9;i++){
				// divisors.push_back(isNotPrime(stored_val[i]));
				// cout << "printing divisors \n";
				cout << isPrime(stored_val[i]) << " ";

			}
			cout << endl;
		}
		if (index == num_outputs)
			{
				// cout << num_outputs << endl;
				break;
			}
		
}
}