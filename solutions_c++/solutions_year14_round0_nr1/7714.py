#include <iostream>

using namespace std;

int m1[4][4], m2[4][4];

int main() {
	// freopen("in.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);
	int T;

	cin >>T;

	for(int t = 0; t < T; t++) {
		int a, b;
		cin >>a;
		a--;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >>m1[i][j];

		cin >>b;
		b--;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >>m2[i][j];

		bool badMagician = false;
		int ans = -1;
		for(int i = 0; i < 4 && !badMagician; i++) {
			for(int j = 0; j < 4 && !badMagician; j++) {
				if(m1[a][i] == m2[b][j]) {
					if(ans != -1)
						badMagician = true;
					ans = m1[a][i];
				}
			}
		}

		cout <<"Case #" <<t + 1 <<": ";
		if(badMagician)
			cout <<"Bad magician!" <<endl;
		else if(ans != -1)
			cout <<ans <<endl;
		else
			cout <<"Volunteer cheated!" <<endl;
	}
	return 0;
}