#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define forn(a,n) for(int a = 0; a<(n); ++a)

vector<int> intersecar(vector<int> &a, vector<int> &b) {
	vector<int> ret;
	forn(i,4) {
		bool esta = false;
		forn(j,4)
			esta |= a[i] == b[j];
		if(esta)
			ret.push_back(a[i]);
	}
	return ret;
}

int T, mapa[6][6];
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	scanf("%i", &T);
	forn(t,T) {
		int row;
		vector<int> r1, r2;
		scanf("%i", &row);
		forn(i,4) forn(j,4)
			scanf("%i", &mapa[i][j]);
		forn(j,4) r1.push_back(mapa[row-1][j]);
		
		scanf("%i", &row);
		forn(i,4) forn(j,4)
			scanf("%i", &mapa[i][j]);
		forn(j,4) r2.push_back(mapa[row-1][j]);

		vector<int> inter = intersecar(r1,r2);

		printf("Case #%i: ", t+1);

		if(inter.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if(inter.size() == 1) {
			printf("%i\n", inter[0]);
		} else {
			printf("Bad magician!\n");
		}
	}
}