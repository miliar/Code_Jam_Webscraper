#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<vector>
#include<queue>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<functional>
#include<climits>
#define eps 1e-9
const int mod = 1e9 + 7;
using namespace std;

int main(){

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i){
		int a, b, k;
		scanf("%d %d %d", &a, &b, &k);
		int ways = 0;
		for (int j = 0; j < a; ++j){
			for (int p = 0; p < b; ++p){
				if ((j & p) < k) ways++;
			}
		}
		printf("Case #%d: %d\n", i, ways);
	}

	return 0;
}