#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <stdio.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int n, l;

void solve(){
	cin >> n >> l;
	string str[105], bad;
	for(int i=0; i<n; i++) cin >> str[i];
	cin >> bad;
	for(int i=0; i<n; i++){
		if(str[i] == bad){
			puts("IMPOSSIBLE");
			return;
		}
	}
	if(l == 1){
		puts("0 ?");
		return;
	}
	for(int i=0; i<l-1; i++){
		putchar('?');
	}
	printf(" ");
	for(int i=0; i<36; i++){
		printf("01");
	}
	printf("0?");
	for(int i=0; i<36; i++){
		printf("01");
	}
	puts("");
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		solve();
	}
}