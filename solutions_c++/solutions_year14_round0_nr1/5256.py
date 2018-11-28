#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <memory.h> 
#include <math.h> 
#include <assert.h> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <string> 
#include <functional> 
#include <vector> 
#include <deque> 
#include <utility> 
#include <bitset> 
#include <limits.h>  

using namespace std; 
typedef long long ll; 
typedef unsigned long long llu; 
typedef double lf;
typedef unsigned int uint;
typedef long double llf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
#define memset0(x) memset(x, 0, sizeof (x));
int TC, TCC;

bool CA[17], CB[17];
int QA, QB;
vector<int> res;

void init () {
	memset0(CA);
	res.clear();
	memset0(CB);
}

void solve () {
	scanf("%d", &QA);
	for(int i = 1; i <= 4; i++) {
		for(int j = 1; j <= 4; j++) {
			int x; scanf("%d", &x);
			if(i == QA) CA[x] = 1;
		}
	}
	scanf("%d", &QB);
	for(int i = 1; i <= 4; i++) {
		for(int j = 1; j <= 4; j++) {
			int x; scanf("%d", &x);
			if(i == QB) CB[x] = 1;
		}
	}

	for(int i = 1; i <= 16; i++) {
		if(CA[i] && CB[i]) res.push_back(i);
	}

	printf("Case #%d: ", TCC);
	if(res.empty()) puts("Volunteer cheated!");
	else if(res.size() > 1) puts("Bad magician!");
	else printf("%d\n", res[0]);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &TC);
	while(++TCC <= TC) {
		init();
		solve();
	}
	return 0;
}