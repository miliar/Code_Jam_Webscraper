#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <vector>
#include <unordered_map>

using namespace std;

void changeBase(int num, int base)
{
	if (num == 0)
		return;
	int r = num % base;
	num /= base;
	changeBase(num, base);
	cout << r;
	return;
}

long long toBase(long long binary, int base) {
	long long bin, dec = 0, rem;
	int i = 0;
	while (binary > 0)
	{
		rem = binary % 10;
		dec = dec + rem * pow(base, i);
		//base = base * base;
		binary = binary / 10;
		i++;
	}
	return dec;
}

vector<string> generateCoin(int N) {
	vector<string> coins;
	if (N == 1) {
		coins = { "0", "1" };
		return coins;
	}
	for (auto coin : generateCoin(N - 1)) {
		coins.push_back("1" + coin);
		coins.push_back("0" + coin);
	}
	return coins;
}

void getDivisors(string coin, vector<int>& divisors) {
	for (int base = 2; base < 11; ++base) {
		long long decimal = toBase(stoll(coin), base);
		bool prime = true;
		for (int divisor = 2; divisor <= ceil(sqrt(decimal)); ++divisor) {
			if (decimal % divisor == 0)
			{
				divisors.push_back(divisor);
				prime = false;
				break;
			}
		}
		if (prime) {
			break;
		}
	}
}

void generateCoinJam(vector<string>& coins,int J ,unordered_map<string, vector<int>>& jamCoins) {

	string coin;
	
	for (auto itr = begin(coins); itr != end(coins); ++itr)	{
		coin = "1" + *itr + "1";
		vector<int> divisors;
		divisors.reserve(10);
		getDivisors(coin, divisors);
		if (divisors.size() == 9) {
			jamCoins[coin] = divisors;
		}
		if (jamCoins.size() == J) {
			break;
		}
	}
}

int main() {
	
	ifstream input("C-small-attempt1.in");
	ofstream output("output-large.txt");

	int T; //test cases
	input >> T;
	for (int i = 1; i <= T; ++i){
		int N, J;
		input >> N >> J;

		unordered_map<string, vector<int>> mapOfCoins;
		
		vector<string> coins = generateCoin(N - 2);
		generateCoinJam(coins, J,mapOfCoins);
		output << "Case #" << i << ":" <<endl;	
		for (auto iter = begin(mapOfCoins); iter != end(mapOfCoins); ++iter){
			output << iter->first << " ";
			for (auto divisorItr = begin(iter->second); divisorItr != end(iter->second); ++divisorItr) {
				output << *divisorItr << " ";
			}
			output << endl;
		}
	}
	output.close();

	return 0;
}