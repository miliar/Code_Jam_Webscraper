#include<bits/stdc++.h>

using namespace std;

bool check(int x, int r, int c) {
	if (x > 6) return false;
	if ((x > r)) return false;
	if ((x >= 2 * c + 1)) return false;
	if ((r * c) % x != 0) return false;
	
	if (x <= 3) return true;
	
	int a = x / 2;
	int b = x - a;
	
	if ((r > b) && (c > a)) return true;
	
	if ((x == 4) && (c == 2)) return false;
	if ((x == 6) && (c == 3)) return false;
	   
	return true; 
}

int main() {
	
	freopen("F:\\Dev C++\\D-small-attempt0.in", "r", stdin);
	freopen("F:\\Dev C++\\D-small-attempt0.out", "w", stdout);
	
	int x, r, c, temp, tc;
	scanf("%d", &tc);

	for(int k=1; k<=tc; k++) {
		scanf("%d %d %d", &x, &r, &c);
		if (r < c) {
			temp = r;
			r = c;
			c = temp;
		} 		 
		
		if (check(x, r, c)) printf("Case #%d: GABRIEL\n", k);
		else printf("Case #%d: RICHARD\n", k);
	}
}
