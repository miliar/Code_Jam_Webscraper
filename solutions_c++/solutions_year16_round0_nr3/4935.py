#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <bitset>
using namespace std;

typedef vector <int> vi;

long long isPrime (long long number){
	for(long long i = 2; i < sqrt(number); i++){
		if(number%i == 0) return i;
	}
	return 0;
}

long long changeBase(long long coin, int N, int base){
	long long answer;
	answer = strtoll((to_string(coin)).c_str(), nullptr, base);
	return answer;
}

vector <long long> coinGen(){
	int i;
	long long coin = ((long long) pow(2, 15)) + 1;
	vector <long long> coins;
	for(i = 0; i < 1000; i += 2){
		coins.push_back(strtoll(((bitset <16> (coin + i)).to_string()).c_str(), nullptr, 10));
	}
	return coins;
}

int main(){
	int N, J, i, T, k;
	cin >> T >> N >> J;
	vector <long long> coins(coinGen());
	long long coin = 0;
	cout << "CASE #1:\n";
	for(i = 0; J > 0; i++){
		coin = coins[i];
		vi divisors;
		bool isValid = true;
		for(k = 2; k <= 10; k++){
			long long temp = isPrime(changeBase(coin, N, k));
			if(temp == 0){
				isValid = false;
				break;
			}
			else divisors.push_back(temp);
		}
		if(isValid){
			J--;
			cout << coin << " ";
			for(k = 0; k < divisors.size(); k++){
				cout << divisors[k] << " ";
			}
			cout << "\n";
		}
	}
	return 0;
}