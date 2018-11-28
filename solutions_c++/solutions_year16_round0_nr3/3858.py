#include <cstdio>
#include <cstdlib>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

void printv(vll v) { for(ll i : v) cout << i << " "; cout << endl;}

//returns first known divisor, -1 otherwise
ll isprime(ll num) {
	ll maxi = (ll)sqrtl(num);
	for (ll i = 2; i <= maxi; i++) {
		if (num % i == 0) return i;
	}
	return -1;
}

ll changebase(ll num, int base) {
	std::string s = std::bitset< 64 >(num).to_string();
	return stoll(s, nullptr, base);
}

int main() {
	int n, j;
	scanf("%d %d", &n, &j);
	printf("Case #1: \n");
	int start = (ll)pow(2, n-1) + 1;
	int end = (ll)pow(2, n);
	
	for (int num = start; j > 0 && num < end; num+=2) {
		bool flag = true;
		vll divisors;
		for (int base = 2; base <= 10; base++) {
			ll numb = changebase(num, base);
			ll p = isprime(numb);
			if (p < 0) {
				flag = false;
				break;
			}
			divisors.push_back(p);
		}
		if (flag) {
			cout << stoll(std::bitset< 64 >(num).to_string()) << " ";
			
			printv(divisors);
			j--;
		}
	}
}
