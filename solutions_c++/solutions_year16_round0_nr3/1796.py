#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <limits.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <deque>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int cnt;

void printb(lint x){
	if(x == 0) return;
	printb(x/2);
	printf("%lld",x%2);
}

bool ok(lint x, int base, int quot){
	int cnt = 0, power = 1;
	while(x){
		cnt += (x&1) * (power);
		x >>= 1;
		power *= base;
		power %= quot;
	}
	return cnt % quot == 0;
}

void backtrack(lint x, int y){
	if(y == 32){
		int divisor[11] = {};
		set<int> s;
		for(int j=2; j<=10; j++){
			for(int k=2; k<=50; k++){
				if(s.find(k) != s.end()) continue;
				if(ok(x, j, k)){
					s.insert(k);
					divisor[j] = k;
					break;
				}
			}
			if(!divisor[j]) return;
		}
		printb(x);
		for(int j=2; j<=10; j++){
			printf(" %d",divisor[j]);
		}
		puts("");
		cnt++;
		if(cnt == 500){
			exit(0);
		}
		return;
	}
	if(y != 0 && y != 31) backtrack(x, y+1);
	backtrack(x + (1ll<<y), y+1);
}

int main(){
	puts("Case #1:");
	backtrack(0, 0);
	puts("NOT OK");
}