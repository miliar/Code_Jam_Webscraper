#define _CRT_SECURE_NO_WARNINGS
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<vector>
#include<cctype>
#include<bitset>
#include<sstream>
#include<stdio.h>
#include<cstring>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<limits.h>
#define mp make_pair
using namespace std;
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int main(){
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
#endif
		int t;
		int a, b, c;
		scanf("%d", &t);
		for (int i = 1; i <= t; ++i){
			scanf("%d%d%d", &c, &a, &b);
			if (a > b)
				swap(a, b);
			printf("Case #%d: ", i);
			if (c == 1)
				puts("GABRIEL");
			if (c == 2){
				if ((a*b) % 2 == 0)
					puts("GABRIEL");
				else
					puts("RICHARD");
			}
			if (c == 3){
				if (a == 2 && b == 3)
					puts("GABRIEL");
				else if (a == 3 && b == 3)
					puts("GABRIEL");
				else if (a == 3 && b == 4)
					puts("GABRIEL");
				else
					puts("RICHARD");
			}
			if (c == 4){
				if (a == 3 && b == 4)
					puts("GABRIEL");
				else if (a == 4 && b == 4)
					puts("GABRIEL");
				else
					puts("RICHARD");
			}
		}
		return 0;
	}