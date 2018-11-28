#include "iostream"
#include "stdio.h"
#include "vector"
#include "queue"
#include "algorithm"
#define MAXN 65536
using namespace std;

vector<int> primes;
int num[65550];

void generateprime() {
	for (int i = 2; i<= MAXN; i++) {
		if (num[i]!=0) continue;
		primes.push_back(i);
		for (int j = i; j <= MAXN; j+=i) {
			num[j]=1;
		}
	}
}
string nextstr(string str) {
	for (int i = str.length() - 2; i>=0; i--) {
		if (str[i] == '0') {
			str[i] = '1';
			return str;
		}
		else {
			str[i] = '0';
		}
	}
}
int main() {
	generateprime();
	// freopen("B-large.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T;
	cin >> T;
	for (int cst = 1; cst <= T; cst++) {
		cout << "Case #" << cst << ": "<<endl;
		int N, J;
		cin >> N >> J;
		string str;
		str += '1';
		for (int i = 1; i < N - 1; i++)
			str += '0';
		str += '1';
		int count = 0;
		while (count < J) {
			int jamcoin = 1;
			for (int i = 2; i<=10; i++) {
				long long value = 0;
				long long base = 1;
				for (int j = N - 1; j >= 0; j--) {
					value += base * (str[j] - '0');
					base = base * i;
				}
				int isprime = 0;
				for (int j = 0; j < primes.size(); j++) {
					if (value % primes[j] == 0 && primes[j]!=value) {
						isprime = 1;
						// cout << primes[j] << " ";
						break;
					}
				}
				if (isprime == 0) {
					jamcoin = 0;
					break;
				} 
			}
			if (jamcoin) {
				cout << str << " ";
				for (int i = 2; i<=10; i++) {
					long long value = 0;
					long long base = 1;
					for (int j = N - 1; j >= 0; j--) {
						value += base * (str[j] - '0');
						base = base * i;
					}
					int isprime = 0;
					for (int j = 0; j < primes.size(); j++) {
						if (value % primes[j] == 0 && primes[j]!=value) {
							isprime = 1;
							cout << primes[j] << " ";
							break;
						}
					}
				}
				cout << endl;
				count++;
			}
			str = nextstr(str);
		}
	}	
}