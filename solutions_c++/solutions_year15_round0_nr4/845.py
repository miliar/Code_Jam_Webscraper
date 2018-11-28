#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

bool solve(){
	int X, R, C;
	scanf("%d%d%d", &X, &R, &C);
	if (X == 1) return 0;
	else if (X == 2){
		if (R % 2 == 0 || C % 2 == 0) return 0;
		else return 1;
	}else if (X == 3){
		if (R % 3 == 0 && C > 1 || C % 3 == 0 && R > 1) return 0;
		else return 1;
	}else{
		if (R % 4 == 0 && C > 2 || C % 4 == 0 && R > 2) return 0;
		return 1;
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: %s\n", t, solve() ? "RICHARD" : "GABRIEL");
	}
	return 0;
}
