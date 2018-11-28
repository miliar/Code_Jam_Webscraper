#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

void next_jamcoin(string& coin);
void initial_jamcoin(string& coin, int N);
long long int convert_to_value(string& coin, int base);
bool test_jamcoin(string& coin, long long int* divisors);
long long int convert_to_value(string& coin, int base);
long long int get_divisor(long long int coin_value);
void print_array(long long int *arr, int n);
long long int exponent(int base, int power);

int main(){
	int testNum;
	int N;
	int J;
	int valid_count = 0;
	string coin;

	long long int divisors[9];

	cin >> testNum;
	
	for(int i = 0; i < testNum; i++){
		cin >> N;
		cin >> J;
		cout << "Case #" << i+1 << ":" << endl;

		initial_jamcoin(coin, N);
		while(valid_count < J){
			
			if(test_jamcoin(coin, divisors) == true){
				cout << coin << ' ';
				print_array(divisors, 9);
				valid_count++;
				cerr << valid_count << endl;
			}
			next_jamcoin(coin);

		}
		coin.clear();		
	}
}

void next_jamcoin(string& coin){
	for(int i = coin.length() - 2; i >= 0 ; i--){
		if(coin[i] == '0'){
			coin[i] = '1';

			for(int j = i+1; j < (int)coin.length() - 1; j++){
				coin[j] = '0';
			}
			break;
		}
	}
}

void initial_jamcoin(string& coin, int N){

	coin += '1';
	for(int i = 1; i < N; i++){
		if(i == N-1){
			coin += '1';
		}
		else{
			coin += '0';
		}
	}
}

bool test_jamcoin(string& coin, long long int* divisors){
	long long int coin_value;
	int i = 0;

	for(int base = 2; base <= 10; base++){
		coin_value = convert_to_value(coin, base);

		divisors[i] = get_divisor(coin_value);
		if(divisors[i] == 0){
			return false;
		}
		i++;
	}
	return true;
}

long long int convert_to_value(string& coin, int base){

	long long int coin_value = 0;
	int power = 0;

	for(int i = (int)coin.length() - 1; i >= 0 ; i--){
		if(coin[i] == '1'){
			coin_value += exponent(base, power);
		}
		power++;
	}
	return coin_value;
}

long long int get_divisor(long long int coin_value){
	if(coin_value % 2 == 0){
		return 2;
	}

	for(long long int i = 3; i < (long long int) sqrt((long double)coin_value); i += 2){
		if(coin_value % i == 0){
			return i;
		}
	}

	return 0;
}

void print_array(long long int *arr, int n){
	for(int i = 0; i < n; i++){
		cout << arr[i] << ' ';
	}
	cout << endl;
}

long long int exponent(int base, int power){
	long long int total = 1;

	for(int i = 1; i <= power; i++){
		total *= base;
	}
	return total;
}