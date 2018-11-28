#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <utility>
using namespace std;

int t, T = 1;

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &t);
	while(t--){
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		if(x == 1) printf("Case #%d: GABRIEL\n", T++);
		else if(x == 2){
			if(r == 1 && c == 1) printf("Case #%d: RICHARD\n", T++);
			else if((r == 1 && c == 3) || (r == 3 && c == 1)) printf("Case #%d: RICHARD\n", T++);
			else if(r == 3 && c == 3) printf("Case #%d: RICHARD\n", T++);
			else printf("Case #%d: GABRIEL\n", T++);
		}
		else if(x == 3){
			if(r == 1 || c == 1) printf("Case #%d: RICHARD\n", T++);
			else if((r == 2 && c == 3) || (r == 3 && c == 2)) printf("Case #%d: GABRIEL\n", T++);
			else if((r == 3 && c == 4) || (r == 4 && c == 3)) printf("Case #%d: GABRIEL\n", T++);
			else if(r == 3 && c == 3) printf("Case #%d: GABRIEL\n", T++);
			else printf("Case #%d: RICHARD\n", T++);
		}
		else if(x == 4){
			if(r == 4 && c == 4) printf("Case #%d: GABRIEL\n", T++);
			else if((r == 3 && c == 4) || (r == 4 && c == 3)) printf("Case #%d: GABRIEL\n", T++);
			else printf("Case #%d: RICHARD\n", T++);
		}
	}
	return 0;
}
