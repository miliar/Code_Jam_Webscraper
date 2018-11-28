//gcj D

#include <iostream>
#include <string.h>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
using namespace std;

#define LL __int64
#define MOD 1000000007

int X, R, C;

int solve(){
	if (X > R*C) 
		return 0;
	if (X == 1){
		if (R == 1 && C == 1) 
			return 1;
		return 1;
	}
	if (X == 2){
		if (R == 1){
			if (C == 4 || C == 2) 
				return 1;
			return 0;
		}
		if (R == 2) 
			return 1;
		if (R == 3){
			if (C == 3) 
				return 0;
			return 1;
		}
		if (R == 4) 
			return 1;
	}
	if (X == 3){
		if (R == 1) 
			return 0;
		if (R == 2){
			if (C == 3) return 1;
			return 0;
		}
		if (R == 3) 
			return 1;
		if (R == 4) 
			return 0;
	}
	if (X == 4){
		if (R == 3 && C == 4) 
			return 1;
		if (R == 4 && C == 4) 
			return 1;
		return 0;
	}
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, ca = 1;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ca++);
		scanf("%d%d%d", &X, &R, &C);
		if (R > C) 
			swap(R, C);
		if (solve() == 0)
			printf("RICHARD\n");
		else printf("GABRIEL\n");
	}
	return 0;
}