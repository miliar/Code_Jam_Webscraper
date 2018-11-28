#include <stdio.h>
#include <string.h>
#define MAXLEN 10009

char s[MAXLEN + 9];
int num[8][8] = { { 0, 1, 2, 3, 4, 5, 6, 7 }, { 1, 0, 3, 2, 5, 4, 7, 6 }, { 2, 3, 1, 0, 6, 7, 5, 4 }, { 3, 2, 0, 1, 7, 6, 4, 5 }, { 4, 5, 7, 6, 1, 0, 2, 3 }, { 5, 4, 6, 7, 0, 1, 3, 2 }, { 6, 7, 4, 5, 3, 2, 1, 0 }, { 7, 6, 5, 4, 2, 3, 0, 1 } };


int mul(int x, int y){
	return num[x][y];
}

int reduce_c(char x){
	if (x == 'i')
		return 2;
	if (x == 'j')
		return 4;
	if (x == 'k')
		return 6;
}

int reduce(char *s){
	int ret;
	ret = 0;
	for (int i = 0; i < strlen(s); i++){
		ret = mul(ret, reduce_c(s[i]));
	}
	return ret;
}






int work123(int kk){
	int n, m, t, p[3], min1, min2;
	scanf("%d %d\n", &n, &m);
	scanf("%s\n", &s);
	t = 0;
	p[0] = reduce(s);
	p[1] = mul(p[0], p[0]);
	p[2] = mul(p[1], p[0]);
	for (int i = 0; i < m; i++){
		t = mul(t, p[0]);
	}

	if (t != 1){
		printf("Case #%d: NO\n", kk + 1);
		return 0;
	}
	min1 = -1;
	min2 = -1;
	t = 0;
	for (int j = 2; j >= 0; j --){
		if (p[j] == 2){
			min1 = (j + 1)*n;
		}
	}

	for (int i = 0; i < strlen(s); i++){
		t = mul(t, reduce_c(s[i]));
		if (t == 2){
			if (min1<0 || (min1>0 && ((i + 1) < min1))){
				min1 = i + 1;
			}
		}
		else{
			for (int j = 2; j >= 0; j--){
				if (mul(p[j],t) == 2){
					if (min1<0 || (min1>0 && ((i + 1 + (j+1)*n) < min1))){
						min1 = i + 1 + (j + 1)*n;
					}
				}
			}
		}
	}

	for (int j = 2; j >= 0; j--){
		if (p[j] == 6){
			min2 = (j + 1)*n;
		}
	}

	t = 0;
	for (int i = strlen(s) - 1; i >= 0; i --){
		t = mul(t, reduce_c(s[i]));
		if (t == 6){
			if (min2<0 || (min2>0 && ((strlen(s) - i) < min2))){
				min2 = strlen(s) - i;
			}
		}
		else{
			for (int j = 2; j >= 0; j--){
				if (mul(t, p[j]) == 6){
					if (min2<0 || (min2>0 && ((strlen(s) - i + (j + 1)*n) < min2))){
						min2 = strlen(s) - i + (j + 1)*n;
					}
				}
			}
		}
	}

	long long x, y, z;
	y = n*m;
	x = min1;
	z = min2;
	y = y - x - z;
	if (y > 0 && x>0 && z>0){
		printf("Case #%d: YES\n", kk + 1);
	}
	else{
		printf("Case #%d: NO\n", kk + 1);
	}

	return 0;
}


int main(){
	int tc, i, j;
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);
	scanf("%d", &tc);
	for (i = 0; i < tc; i++){
		work123(i);
	}
	return 0;
}