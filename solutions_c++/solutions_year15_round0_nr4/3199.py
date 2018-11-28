//mishraiiit
#include <bits/stdc++.h>
using namespace std;
int main() {
	int t, x, y, z;
	cin >> t;

	for(int i = 0; i < t; i++) {
		bool flag = false;
		printf("Case #%d: ",i+1);
		cin >> x >> y >> z;
		flag = (x == 1) || (x == 2 && (!((y * z) & 1))) || (x == 3 && ((y == 2 && z == 3) || (y == 3 && z == 2) || (y == 3 && z == 4) || (y == 4 && z  == 3) || (y == 3 && z == 3))) || (x == 4 && ((y == 4 && z == 4) || (y == 3 && z == 4) || (y == 4 && z == 3)));
		puts((flag)?"GABRIEL":"RICHARD");
	}
	return 0;
}
