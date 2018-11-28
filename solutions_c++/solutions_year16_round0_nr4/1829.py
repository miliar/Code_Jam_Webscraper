#include "StdAfx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main(int argc, char** argv){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf(" %d", &tt);
	for (int qq = 1; qq <= tt; qq++){
		int x, r, c, res = 1;
		scanf(" %d %d %d", &x, &r, &c);
		if (x == 1) res = 2;
		if (x == 2 && (r * c) % 2 == 0) res = 2;
		if (x == 3 && (r * c) % 3 == 0 && min(r, c) >= 2) res = 2;
		if (x == 4 && (r * c) % 4 == 0 && min(r, c) >= 3) res = 2;
		if (x == 5 && (r * c) % 5 == 0 && (min(r, c) >= 4 || (min(r, c) == 3 && max(r, c) > 5))) res = 2;
		if (x == 6 && (r * c) % 6 == 0 && min(r, c) >= 4) res = 2;
		printf("Case #%d: %s\n", qq, res == 1? "RICHARD" : "GABRIEL");
	}
}

