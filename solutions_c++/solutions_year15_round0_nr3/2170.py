#include<cstdio>
#include<cstring>
#include<algorithm>

#define L 10005

using namespace std;

char str[L];
int table[5][5] = {
	{0,},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}};
bool func(char *str, int l, int x) {
	int n = 1, s = 1;
	for (int i = 0; i < l; i++) {
		int j = str[i] - 'i' + 2;
		n = table[n][j];
		if (n < 0) 
			n = -n, s = -s;
		//printf("i : %d, n: %d s: %d\n", i, n, s);
	}
	int nn = n, ss = s;
	for (int i = 1; i < x; i++) {
		nn = table[nn][n];
		ss *= s;
		if (nn<0) 
			nn = -nn, ss = -ss;
		//printf("i : %d, nn: %d ss: %d\n", i, nn, ss);
	}
	//printf("l: %d x: %d s: %d n: %d\n", l, x, s, n);
	if (!(nn==1 && ss == -1))
		return false;

	int mini = -1;
	n = 1, s = 1;
	for (int ii = 0; ii < l * 4; ii++) {
		int i = ii % l;
		int j = str[i] - 'i' + 2;
		n = table[n][j];
		if (n < 0) 
			n = -n, s = -s;
		if (n == 2 && s == 1) {
			mini = ii;
			break;
		}
	}
	if (mini == -1)
		return false;
	//printf("mini: %d s %d n %d\n", mini, s, n);

	int maxk = -1;
	n = 1, s = 1;
	for (int ii = l*4-1; ii >=0; ii--) {
		int i = ii % l;
		int j = str[i] - 'i' + 2;
		n = table[j][n];
		if (n<0)
			n = -n, s = -s;
		//printf("i : %d, n: %d s: %d\n", i, n, s);
		if (n == 4 && s == 1) {
			maxk = l*4-1 - ii;
			break;
		}
	}
	//printf("maxk: %d s %d n %d\n", maxk, s, n);
	if (maxk == -1)
		return false;

	if (mini + maxk +2 >= l*x)
 	  return false;
	return true;
}

int main(){
	int tcc;
	bool ans;
	scanf("%d", &tcc);
	for (int tc = 1; tc <= tcc; tc++) {
		int l, x;
		scanf("%d %d", &l, &x);
		scanf("%s", str);
		if (x >= 24)
			x = x%12 + 12;
		ans = func(str, l, x);
		printf("Case #%d: %s\n", tc, (ans)? "YES":"NO");
	}
	return 0;
}
