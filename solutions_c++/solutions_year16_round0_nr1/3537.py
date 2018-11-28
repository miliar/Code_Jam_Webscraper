#include <bits/stdc++.h>
using namespace std;

bool byl[100];

int policz (long long n, int ile) {
	while (n!=0) {
		int x= n% 10;
		n/=10;
		if (byl[x]==false) {
			ile++;
			byl[x]=true;
		}
	}
	return ile;
}

int main () {
	ios_base::sync_with_stdio(0);
	int t, n;
	cin >> t;
	for (int x=1; x<=t; x++) {
		cin >> n;
		cout << "Case #" << x << ": ";
		if (n==0) cout << "INSOMNIA\n";
		else {
			int ile=0;
			long long N=0;
			for (int i=0; i<10; i++) byl[i]=false;
			while (ile<10) {
				N+=n;
				ile = policz (N, ile);
			}
			cout << N << "\n";
		}
	}
}