#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
struct q{
	int p, r, s;
	inline q operator+(q a) {
		return{ p+a.p, r+a.r, s+a.s };
	}
}level[15][3];
int order[15][3];
//p,r,s
#define P 0
#define R 1
#define S 2
int make_order(int a, int b){
	int t;
	if (a > b){
		swap(a, b);
	}
	if (a == 0 && b == 1)
		return 0;
	if (a == 0 && b == 2)
		return 1;
	if (a == 1 && b == 2)
		return 2;
}
void go(int n, int x){
	if (n == -1){
		if (x == P)
			printf("P");
		else if (x == R)
			printf("R");
		else
			printf("S");
	}
	else{
		if (x == P){
			if (order[n][P] > order[n][R]){
				go(n - 1, R); go(n - 1, P);
			}
			else{
				go(n - 1, P); go(n - 1, R);
			}
		}
		else if (x == R){
			if (order[n][S] > order[n][R]){
				go(n - 1, R); go(n - 1, S);
			}
			else{
				go(n - 1, S); go(n - 1, R);
			}
		}
		else if (x == S){
			if (order[n][P] > order[n][S]){
				go(n - 1, S); go(n - 1, P);
			}
			else{
				go(n - 1, P); go(n - 1, S);
			}

		}
	}
}
int main(){
	level[0][P].p = 1;
	level[0][R].r = 1;
	level[0][S].s = 1;
	order[0][P] = 0;
	order[0][R] = 1;
	order[0][S] = 2;
	for (int i = 1; i <= 12; i++){
		level[i][P] = level[i - 1][P] + level[i - 1][R];
		level[i][R] = level[i - 1][S] + level[i - 1][R];
		level[i][S] = level[i - 1][P] + level[i - 1][S];
		order[i][P] = make_order(order[i - 1][P], order[i - 1][R]);
		order[i][R] = make_order(order[i - 1][S], order[i - 1][R]);
		order[i][S] = make_order(order[i - 1][P], order[i - 1][S]);
	}
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		printf("Case #%d: ", test);
		int n, p, r, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);
		if (level[n][P].p == p && level[n][P].r == r && level[n][P].s == s)
			go(n-1, P);
		else if (level[n][R].p == p && level[n][R].r == r && level[n][R].s == s)
			go(n-1, R);
		else if (level[n][S].p == p && level[n][S].r == r && level[n][S].s == s)
			go(n-1, S);
		else{
			printf("IMPOSSIBLE\n");
			continue;
		}
		printf("\n");
	}
	return 0;
}
