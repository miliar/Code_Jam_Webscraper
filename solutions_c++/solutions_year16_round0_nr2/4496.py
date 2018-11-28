#include <iostream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

char a[10000];
int b[10000];

int work(int r,int need) {
	if (r==0) {
		if (b[r]==need) 
			return 0;
		else
			return 1;
	}
	
	if (b[r]==need) {
		return work(r-1, need);
	}
	else {
		return 1 + work(r-1, 1-need);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ii = 1; ii <= t; ii++) {
		printf("Case #%d: ", ii);
		scanf("%s", a);
		int size = strlen(a);
		for (int i = 0; i < size; i++) {
			if (a[i] == '+')
				b[i] = 1;
			else
				b[i] = 0;
		}
		int ans = work(size - 1,1);
		printf("%d\n", ans);
	}
}