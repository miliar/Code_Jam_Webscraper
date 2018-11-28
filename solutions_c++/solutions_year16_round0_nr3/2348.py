#include <iostream>
#include <algorithm>
using namespace std;

string s = "1000000000000001";
int p[40000000], np;

int isprime(long long x) {
	for(int i = 0; i < np; i++) {
		if(p[i] == x)	
			return 1;
		if(x % p[i] == 0)
			return p[i];
	}
	return 1;
}

int isprimeb(long long b) {
	long long x = 0;
	for(int i = 0; i < s.size(); i++) {
		x *= b;
		x += s[i] - '0';
	}
	//cout << s << " " << b << " " << x << " " << isprime(x) << endl;
	return isprime(x);
}

long long val(long long b) { 
	long long x = 0;
	for(int i = 0; i < s.size(); i++) {
		x *= b;
		x += s[i] - '0';
	}
	return x;
}

void sieve() {
	for(int i = 2; i < 40000000; i++)
		p[i] = 1;
	for(int i = 2; i < 40000000; i++)
		if(p[i]) {
			p[np++] = i;
			for(int j = i + i; j < 40000000; j += i)
				p[j] = 0;
		}
//	for(int i = 0; i < np; i++)
//		cout << p[i] << endl;
}

int main() {
	sieve();
	
	int tc, N, J;
	cin >> tc;
	for(int z = 1; z <= tc; z++) {
		cout << "Case #" << z << ":" << endl;
		cin >> N >> J;
		s = "1"; 
		for(int i = 0; i < N - 2; i++)
			s += "0";
		s += "1";
		
		int count = 0;
		for(int z = s.size()-1; z >= 1 && count < J; z--) {
			s[z] = '1';
			do {
				int ok = 1;
				for(int i = 2; i <= 10; i++)
					if(isprimeb(i) == 1)
						ok = 0;
				if(ok) {
					cout << s;
					for(int i = 2; i <= 10; i++)
						//cout << " " << val(i) << "(" << isprimeb(i) << ")";
						cout << " " << isprimeb(i);
					cout << endl;
					count++;
				}
			} while(count < J && next_permutation(s.begin()+1,s.begin()+s.size()-1));
		}
	}
	
}
