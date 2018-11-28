#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	string X;
	char S[5000];
	int ini, fim, c;

	cin >> c;
	for(int i = 1; i <= c; i++) {
		cin >> X;
		cout << "Case #" << i << ": ";

		ini = 2500;
		fim = 2501;
		S[2500] = X[0];
		for(int j = 1; X[j] != '\0'; j++) {
			if(X[j] < S[ini]) {
				S[fim] = X[j];
				fim++;
			} else {
				S[ini-1] = X[j];
				ini--;
			}
		}

		for(int j = ini; j < fim; j++)
			cout << S[j];
		cout << endl;
		
	}

	return 0;
}