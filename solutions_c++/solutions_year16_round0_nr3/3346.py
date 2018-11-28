#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll _sieve_size;
bitset<66536> bs;
vi primes;

void sieve(ll upperbound) {  // <-- Preprocess
  _sieve_size = upperbound + 1;
  bs.set(); bs[0] = bs[1] = 0;
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back((int)i);
} } 

bool isPrime(ll N) {  // <-- Queries
  if (N <= _sieve_size) return bs[N];
  for (int i = 0; i < (int)primes.size(); i++)
    if (N % primes[i] == 0) return false;
  return true;
}

ull inter(unsigned int n, int base){
	ull r = 0, act = 1;
	for(int i = 0; i < 32; i++){
		if((n & (1 << i)) != 0){
			r += act;
		}
		act *= base;
	}
	return r;
}

int main(){
	int T, N, J;
	sieve(66036);
	unsigned int num = 1, maxim;
	cin >> T >> N >> J;
	cout << "Case #1:" << endl;
	num |= 1 << (N - 1);
	maxim = (1 << N) - 1;

	while(num <= maxim && J > 0){
		bool flag = true;
		for(int i = 2; i <= 10; i++){
			flag &= !isPrime(inter(num,i));
			if(!flag) break;
		}

		if(flag){
			cout << inter(num,10);
			vi w;
			for(int i = 2; i <= 10; i++){
				ull a = inter(num, i);
				for(int j = 0; j < a; j++){
					if(a % primes[j] == 0){
						cout << " " << primes[j];
						break;
					}
				}
			}
			cout << endl;
			J--;
		}
		num += 2;
	}

	
}
