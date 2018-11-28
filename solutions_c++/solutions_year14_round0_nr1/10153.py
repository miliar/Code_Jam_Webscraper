#include <iostream>
#include <set>
#include <vector>
#include <cstdio>

#define forn(i,n) for(int i=0;i<int(n);++i)

using namespace std;

int main() {
	//freopen("magic.in", "r", stdin);
	int T;
	cin >> T;
	int n;
	int m1[4][4], m2[4][4], i1, i2;
	forn (t,T) {
		cout << "Case #" << t+1 << ": ";

		cin >> i1;
		i1--;
		forn (i,4)
			forn (j,4) 
				cin >> m1[i][j];

		cin >> i2;
		i2--;
		forn (i,4)
			forn (j,4) 
				cin >> m2[i][j];

		int c = 0, guessed;
		forn (j1,4) {
			forn (j2,4) {
				if (m1[i1][j1] == m2[i2][j2]) {
					c++;
					guessed = m1[i1][j1];
				}
			}
		}

		if (c==0)
			cout << "Volunteer cheated!";
		else if (c==1)
			cout << guessed;
		else
			cout << "Bad magician!";

		cout << endl;;
	}
	return 0;
}