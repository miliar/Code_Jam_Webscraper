#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector <double> vd;

int tc,n;
vd N,K;

int main() {
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	cin >> tc;
	int count = 0;
	while (tc--) {
		cin >> n;
		N = vd(); K = vd();
		double tmp;
		for (int i=0; i<n; i++) {
			cin >> tmp;
			N.push_back(tmp);
		}
		for (int i=0; i<n; i++) {
			cin >> tmp;
			K.push_back(tmp);
		}
		sort(N.begin(),N.end());
		sort(K.begin(),K.end());
		int i,j,NWin,DNWin;
		i = j = NWin = 0;
		while (i < n || j < n) {
			if (j == n) {
				i++; NWin++;
			}
			else if (N[i] < K[j]) {
				i++; j++;
			}
			else if (N[i] > K[j]) {
				j++;
			}
		}
		i = j = DNWin = 0;
		int maxJ = n;
		while (i < n || j < maxJ) {
			if (N[i] > K[maxJ - 1]) {
				i++; j++; DNWin++;
			}
			else if (N[i] < K[j]) { 
				i++; maxJ--; 
			}
			else if (N[i] > K[j]) {
				i++; j++; DNWin++;
			}
		}
		printf("Case #%d: %d %d\n",++count,DNWin,NWin);
	}
}
