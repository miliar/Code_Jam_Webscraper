#include <stdio.h>

int value(char x){
	switch (x){
	case 'i': return 2;
	case 'j': return 4;
	case 'k': return 6;
	default: return -1;
	}
}
int cal[4][4] = {
	{ 0, 2, 4, 6 },
	{ 2, 1, 6, 5 },
	{ 4, 7, 1, 2 },
	{ 6, 4, 3, 1 },
};

int calculate(int x, int y){
	int val = cal[x / 2][y / 2];
	int sign = !(x % 2 == y % 2);
	if (val % 2) return sign ? val - 1 : val;
	return sign ? val + 1 : val;
}

int reverse(int x, int y){
	int val = calculate(x, y);
	if (x < 2){
		return val % 2 ? val - 1 : val + 1;
	}
	return val;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, m;
	scanf("%d", &t);
	for (m = 0; m < t; m++){
		char str[10001];
		int val[10001];
		int l, x, i, j;
		scanf("%d %d %s", &l, &x, str);
		val[0] = value(str[0]);
		for (i = 1; i < l * x; i++){
			val[i] = calculate(val[i - 1], value(str[i % l]));
		}
		bool able = false;
		for (i = 0; i < l * x - 2; i++){
			if (val[i] == 2){
				for (j = i + 1; j < l * x - 1; j++){
					if (reverse(val[j], val[i]) == 4 &&
						reverse(val[l * x - 1], val[j]) == 6){
						able = true;
						break;
					}
				}
				if (able) break;
			}
		}
		printf("Case #%d: %s\n", m + 1, able ? "YES" : "NO");
	}
	return 0;
}