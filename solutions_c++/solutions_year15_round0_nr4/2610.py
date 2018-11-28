#include <iostream>
#include <cstdio>
using namespace std;

bool solve (int x, int r, int c) {
	if (r > c) return solve (x, c, r);
	if (r == 0 && c == 0) return true;
	if (r*c < x) return true;
	if (x == 1) return false;
	if (x == 2) return (r*c)%2==1;
	if (x == 3 && (r*c)%3 != 0) return true;
	if (x == 4 && (r*c)%4 != 0) return true;
	if (x == 3 && (r == 1 || c == 1)) return true;
	if (x == 3) return false;
	//x == 4
	if (r == 1 || c == 1) return true;
	if (r <= 2 && c <= 2) return true;
	if (r == 2 && c == 4) return true;
	return false;
}

int main()
{
	int db; scanf("%d", &db);
	for (int i = 1; i<=db; i++) {
		int a,b,c; scanf("%d%d%d", &a, &b, &c);
		if (solve(a, b, c)) printf("Case #%d: RICHARD\n", i);
		else printf("Case #%d: GABRIEL\n", i);
	}
    
    
    return 0;
}
