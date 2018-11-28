#include <bits/stdc++.h>
using namespace std;

long long Prime(long long a) {
   	long long i;
   	if (a == 2) return -1LL;
   	if (a % 2 == 0) return 2LL;
   	for(i = 3; i*i <= a && a%i != 0; i += 2);
   	return i;
}
// if (i*i>a) -1, else i
long long po[20][20];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	for (int i=2; i<=10; i++) {
		po[i][0]=1LL;
	}
	for (int j=1; j<=16; j++) {
		for (int i=2; i<=10; i++) {
			po[i][j]=1LL*po[i][j-1]*i;
		}
	}
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
	cout << "Case #" << t << ":\n";
	long long n, J;
	cin >> n >> J;

	for (long long i=0; i<(1<<(n-2)) && J; i++) {
		vector <long long> ans;
		for (int k=2; k<=10; k++) {
			long long a = po[k][0]+po[k][n-1];
			for (int j=0; j<n-2; j++) {
				if ((i>>j)&1LL) a+=po[k][j+1];
			}
			long long prp = Prime(a);
			if (prp==-1 || prp*prp>a) break;
			ans.push_back(prp);
		}
		if (ans.size()==9) {
			J--;
			cout << "1";
			for (int j=n-3; j>=0; j--) cout << ((i>>j)&1LL);
			cout << "1";
			for (auto x : ans) cout << " " << x;
			cout << "\n";
		}
	}
	}
	return 0;
}
