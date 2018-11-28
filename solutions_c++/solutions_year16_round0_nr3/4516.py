#include <iostream>
#include <fstream>

using namespace std;

char filename[] = "factorsTill10power8";
int fact[100000001];
long power[12][22];


void fillPowers() {
	for(long i = 2; i <= 10; ++i) {
		long base = 1;
		for(long j = 0; j <= 20; ++j) {
			power[i][j] = base;
			base *= i;
		}
	}
}

string binaryString(long n) {
	string s = "";
	while(n) {
		s += (char)'0' + (n & 1);
		n >>= 1;
	}
	return s;
}

long isPrime(string s, int b) {
	long k = 0, p = 0;
	for(int i = 0; i < s.size(); ++i) {
		k += (int)(s[i] -'0') * power[b][i];
	}
	for (long i = 2; i*i <= k; ++i) {
		if(!(k % i))
			return i;
	}
	return 0;
}
			
int main (int argc, char * argv[]) {
	int T;
	cin >> T;
	fillPowers();
	for(int t = 1 ; t <= T; ++t) {
		int N, J;
		cin >> N >> J;
		cout << "Case #" << t << ":" << endl;
		int start = (1u << (N - 1)) | 1;
		int end = ~(~(0u) << N);
		
		for(int i = start; i <= end && J; i += 2) {
			long inBase[11];
			bool isValid = true;
			string val = binaryString(i);
			for(int b = 2; b <= 10; ++b){
				inBase[b] = isPrime(val, b);
				if(!inBase[b]) {
					isValid = false;
					break;
				}			
			}
			if(isValid) {
				string a = binaryString(i);
				reverse(a.begin(), a.end());
				cout << a;
				for(int b = 2; b <= 10; ++b) {
					cout << " " << inBase[b];
				}
				--J;
				cout << endl;
			}
		}

	}	
	return 0;
}

