#include <bits/stdc++.h>
using namespace std;

long long int divisor(long long int n) {
	for(long long int i = 2; i <= sqrt(n); i++) 
		if(n % i == 0) 
			return i;
	return -89;
}

string reverse(string s) {
	string rs = "";
	for(int i = s.size()-1; i >= 0; i--)
		rs += s[i];
	return rs;
}

string toBinary(long long int n) {
	if(n == 0) return "0";
	string s = "";
	while (n) {
		if (n & 1)
			s+='1';
		else
			s+='0';
		n >>= 1;
	}
	return s;
}

long long int changeBase(long long int n, int base) {
	string s = toBinary(n);
	long long int number = 0;
	for(int i = 0; i < s.size(); i++) {
		number += (s[i]-'0') * pow(base, i);
	}
	return number;
}

bool isPrime(long long int n) {
	if(n < 2) return false;
	for(long long int i = 2; i <= sqrt(n); i++) 
		if(n % i == 0) 
			return false;
	return true;
}

int main() {
	int t, n, j;
	scanf("%d", &t);
	while(t--){
		scanf("%d %d", &n, &j);
		long long int min = 1 + pow(2, n-1);
		long long int max = pow(2, n) - 1;
		long long int i;
    cout << "Case #1:" << endl;
		while(j--) {
			for(i = min+2; i < max; i+=2){
				if(!isPrime(i)){
					int base = 3;
					while(!isPrime(changeBase(i,base)) && base <= 10) {
					    base++;
					}
					if(base > 10) {
						cout << reverse(toBinary(i)) << " " << divisor(changeBase(i,2)) << " " << divisor(changeBase(i,3)) << " " << divisor(changeBase(i,4)) << " ";
						cout << divisor(changeBase(i,5)) << " " << divisor(changeBase(i,6)) << " " << divisor(changeBase(i,7)) << " " << divisor(changeBase(i,8)) << " ";
						cout << divisor(changeBase(i,9)) << " " << divisor(changeBase(i,10)) << endl;
						break;
					}
				}
			}
			min = i+2;
		}
	}
	return 0;
}