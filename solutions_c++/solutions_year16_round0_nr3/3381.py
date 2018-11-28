#include <bits/stdc++.h>

using namespace std;

bool isPrime(long long n){
	if(n <= 1) return false;
	if(n <= 3) return true;
	if(n % 2 == 0) return false;
	if(n % 3 == 0) return false;
	for(long long i = 5; i <= sqrt(n); i = i+6){
		if(n % i == 0) return false;
		if(n % (i+2) == 0) return false;
	}
	return true;
}

long long AToB(long long n, int a, int b){
	long long num = 0;
	long long base = 1;
	while(n){
		num += (n % b) * base;
		n = n / b;
		base *= a;
	}
	return num;
}

int main(){
	freopen("in.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	int t; cin >> t;
	for(int i = 1; i <= t; i++){
		cout << "Case #1:" << endl;
		int N, J, count = 0;
		cin >> N >> J;
		for(long long j = pow(2, N-1)+1; j <= pow(2, N) && count < J; j = j+2){
			long long tmp = AToB(j, 10, 2);
			int ans = 0;
			
			for(int z = 2; z <= 10; z++){
				long long check = AToB(tmp, z, 10);
				if(isPrime(check) == false) ans++;
			}

			if(ans == 9){
				cout << tmp << " ";
				for(int z = 2; z <= 10; z++){
					long long check = AToB(tmp, z, 10);
					if(check % 2 == 0){
						cout << 2 << " ";
						continue;
					}
					if(check % 3 == 0){
						cout << 3 << " ";
						continue;
					}
					for(int num = 5; num <= sqrt(check); num++){
						if(check % num == 0){
							cout << num << " ";
							break;
						}
						if(check % (num+2) == 0){
							cout << num+2 << " ";
							break;
						}
					}
				}
				cout << endl;
				count++;
			}
		}
	} 
	return 0;
}
