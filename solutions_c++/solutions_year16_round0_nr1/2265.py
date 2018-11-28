#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin >> t;
	int run = 1;
	while(t--) {
		long long int n;
		cin >> n;
		if(n == 0) {
			cout << "Case #" << run++ << ": " << "INSOMNIA" << endl;
		} else {
			int hash[10] = {0};
			long long int i = 1;
			while(i <= 10000) {
				long long int newn = n * i;
				long long int temp = newn;
				while(newn) {
					long long int rem = newn % 10;
					hash[rem] = 1;
					newn /= 10;
				}
				int j;
				int flag = 0;
				for(j = 0; j < 10; j++) {
					if(hash[j] != 1) {
						flag = 1;
					}
				}
				if(!flag) {
					cout << "Case #" << run++ << ": " << temp << endl;
					break;
				}
				i++;
			}
			if(i == 10001) {
				cout << "Case #" << run++ << ": " << "INSOMNIA" << endl;
			}
		}
	}
	return 0;
}