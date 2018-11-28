#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	freopen("a.in","r",stdin);
	freopen("ans.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		int n;
		int x,r,c;
		scanf("%d %d %d", &x, &r, &c);
		printf("Case #%d: ", t);
		if (x > max(r,c) || ((x + 1) > 2 * min(r,c) && x > 2) || r * c % x != 0 || x >= 7){
			printf("RICHARD\n");
		}else	
			printf("GABRIEL\n");
	}
	return 0;
}
