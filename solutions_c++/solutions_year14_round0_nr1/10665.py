#include <bits/stdc++.h>
#define _ std::ios_base::Init i; std::ios_base::sync_with_stdio(false); std::cin.tie(0);
using namespace std;

int main() {
	int t;
	int a[5][5], b[5][5], c1, c2;
	cin >> t;
	for (int cs = 1; cs <= t; cs++){
		cin >> c1;
		for (int i = 0; i<4; i++)
		for (int j = 0; j<4; j++)
			cin >> a[i][j];
		cin >> c2;
		for (int i = 0; i<4; i++)
		for (int j = 0; j<4; j++)
			cin >> b[i][j];
		bool flag = false, bad = false;
		int common = -1;
		c1--;
		c2--;
		for (int i = 0; i<4; i++)
		{
			int n = a[c1][i];
			for (int j = 0; j<4; j++)
			if (b[c2][j] == n){
				if (flag){
					bad = true;

				}
				common = n;
				flag = true;
				break;
			}
			if (bad) break;
		}
		if (bad)
			cout << "Case #" << cs << ": Bad magician!\n";
		else if (common == -1)
			cout << "Case #" << cs << ": Volunteer cheated!\n";
		else
			cout << "Case #" << cs << ": " << common << endl;
	}
	return 0;
}