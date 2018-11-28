#include <bits/stdc++.h>

using namespace std;

int check(int* hash) {
	for(int i = 0; i < 10; i++)
		if(hash[i] == 0)
			return 0;
	return 1;
}

int main()
{
	ios::sync_with_stdio(false);
	long T, N, N_CPY, cont;
	int hash[10];

	cin >> T;
	for(long i = 0; i < T; i++) {
		memset(hash, 0, sizeof hash);
		cin >> N;
		if(N == 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			cont = 1;
			while(!check(hash)) {
				N_CPY = N * cont;
				while(N_CPY != 0) {
					hash[N_CPY%10] = 1;
					N_CPY/=10;
				}
				cont++;
			}
			cout << "Case #" << i+1 << ": " << N*(cont-1) << endl;
		}
	}
	
	return 0;
}