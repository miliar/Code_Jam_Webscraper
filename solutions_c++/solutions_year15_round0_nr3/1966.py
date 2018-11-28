#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
const int mul[5][5] = { { 0, 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };

int Mul(int x, int y){
	int temp = 1;
	if (x < 0){
		x = -x;
		temp *= -1;
	}
	if (y < 0){
		y = -y;
		temp *= -1;
	}
	return temp * mul[x][y];
}

int check(int temp, int x){
	int t = 1, p;
	if (temp == 1){
		return 1;
	}
	else if (temp == -1){
		if (x % 2 == 1){
			return -1;
		}
		else{
			return 1;
		}
	}
	if (temp < 0){
		t = -1;
		temp = -temp;
	}
	if (x % 2 == 0){
		t = 1;
	}
	p = x / 2;
	if (x % 2 == 0){
		if (p % 2 == 1){
			return -1 * t;
		}
		else{
			return t;
		}
	}
	else{
		if (p % 2 == 1){
			return -1 * t *temp;
		}
		else{
			return t * temp;
		}
	}
}

int main()
{
 	freopen("C:\\Users\\Administrator\\Downloads\\a.txt", "r", stdin);
	freopen("C:\\Users\\Administrator\\Downloads\\b.txt", "w", stdout);
	long long n, i, j, len, x, temp, y, _y, _i;
	char s[10001];
	scanf("%I64d", &n);
	for (j = 1; j <= n; j++){
		scanf("%I64d%I64d", &len, &x);
		scanf("%s", s);
		temp = s[0] - 'g';
		for (i = 1; i < len; i++){
			temp = Mul(temp, s[i] - 'g');
		}
		temp = check(temp, x);
		if (temp != -1){
			printf("Case #%I64d: NO\n", j);
			continue;
		}
		temp = s[0] - 'g';
		y = 1;
		i = 1;
		while (temp != 2){
			if (i >= len){
				i = 0;
				y++;
			}
			if (y > x){
				break;
			}
			temp = Mul(temp, s[i++] - 'g');
		}		
		if (temp != 2){
			printf("Case #%I64d: NO\n", j);
			continue;
		}
		_i = i;
		_y = y;
		temp = s[len - 1] - 'g';
		y = x;
		i = len - 2;
		while (temp != 4){
			if (i < 0){
				y--;
				i = len - 1;
			}
			if (y < 1){
				break;
			}
			temp = Mul(s[i--] - 'g', temp);
		}
		if (temp != 4){
			printf("Case #%I64d: NO\n", j);
			continue;
		}
		i += 2;
		if (_y  * len + _i <= y * len + i){
			printf("Case #%I64d: YES\n", j);
			continue;
		}
		printf("Case #%I64d: NO\n", j);
	}
}