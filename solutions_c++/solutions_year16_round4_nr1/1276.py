#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <string.h>

using namespace std;
const int maxN = 30009;
typedef pair<int, int> para;

int n, t, p, r, s, tab[maxN], licz[20];
string ciag[maxN];

int main() {
	ios_base::sync_with_stdio(0);
	int pom = 0;
	cin>>t;
	for (int i = 1; i <= t; i++) {
		cin>>n>>r>>p>>s;
		cout<<"Case #"<<i<<": ";
		int x = pow(2, n);
		for (int j = 1; j <= 3; j++) {
			tab[1] = j;
			for (int k = 1; k < x; k++) {
				if (tab[k] == 1) {
					tab[2 * k] = 1;
					tab[2 * k + 1] = 2;
				}
				
				if (tab[k] == 2) {
					tab[2 * k] = 2;
					tab[2 * k + 1] = 3;
				}
				
				if (tab[k] == 3) {
					tab[2 * k] = 1;
					tab[2 * k + 1] = 3;
				}
			}
			
			for (int k = x; k < 2 * x; k++) {
				licz[tab[k]]++;
			}
			bool tr = true;
			tr = tr && licz[1] == p;
			tr = tr && licz[2] == r;
			tr = tr && licz[3] == s;
			if (tr == 1) {
				for (int k = x; k < 2 * x; k++) {
					if (tab[k] == 1)
						ciag[k / 2] += 'P';
					if (tab[k] == 2)
						ciag[k / 2] += 'R';
					if (tab[k] == 3)
						ciag[k / 2] += 'S';
				}
				
				for (int k = x - 1; k > 1; k -= 2) {
					if (ciag[k - 1].compare(ciag[k]) > 0)
						swap(ciag[k - 1], ciag[k]);
					ciag[k / 2] = ciag[k - 1] + ciag[k];
				}
				cout<<ciag[1]<<"\n"; pom = 1;
			}
			for (int k = 1; k <= 2 * x; k++)
				ciag[k] = "";
			licz[1] = 0; licz[2] = 0; licz[3] = 0;
		}
		if (pom == 0) cout<<"IMPOSSIBLE\n";
		pom = 0;
	}
	return 0;
}
