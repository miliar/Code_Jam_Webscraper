#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

typedef long long ll;
int isP[1000010] = { 0 };
ll Ps[1000010];
ll pN;


void init()
{
	ll mV = 1000000;
	ll i, j;

	for (i = 2; i <= mV; i++)
		isP[i] = 1;
	for (i = 2; i <= mV; i++) if (isP[i])
	{
		Ps[pN++] = i;
		for (j = i*i; j <= mV && i <= 1000; j += i)
			isP[j] = 0;
	}
}


long long power(long long base, int index){
	long long result = 1;
	for (int i = 0; i < index; i++)
		result *= base;
	return result;
}

long long isPrime(long long input){
	for (ll i = 0; i < pN; i++){
		if (input != Ps[i] && input%Ps[i] == 0)
			return Ps[i];
	}
	return -1;
}

ll toBinary(ll input){
	for (int i = 15; i >= 0; i--){
		if (input >= power(2, i)){
			cout << 1;
			input -= power(2, i);
		}
		else
			cout << 0;
	}
}

void solutionC(){
	int N = 16, J = 50;
	cout << "Case #1:" << endl;
	long long tmp = power(2, 15) + 1;
	int count = 0;
	while (count < 50){
		vector<long long> factors;
		for (int base = 2; base <= 10; base++){
			long long buffer = 0;
			for (int i = 0; i < 16; i++)
				if (tmp & (1 << i))
					buffer += power(base, i);
			long long factor = isPrime(buffer);
			if (factor == -1)
				break;
			factors.push_back(factor);
		}
		if (factors.size() == 9){
			count++;
			toBinary(tmp);
			cout <<" ";
			for (int i = 0; i < 9; i++)
				cout << factors[i] << " ";
			cout << endl;
		}
		tmp += 2;
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	init();
	int t;
	cin >> t;
	cin >> t;
	solutionC();
	return 1;
}
