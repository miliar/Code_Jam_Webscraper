/*
ID: george_18
LANG: C++
TASK: 
*/

#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <set>
#include <map>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <string.h>
#include <algorithm>

#define MAXN 
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define X first
#define Y second
#define left(a) (2*(a))
#define right(a) (2*(a)+1)
#define par(a) ((a)/2)
#define PI 3.141592653

using namespace std;

typedef long long int ll;
typedef pair<int,int> pii;

int K,C,S;

void Read(int Case) {
	printf("Case #%d: ", Case);
	scanf("%d %d %d", &K, &C, &S);
	return;
}

void Solve() {
	if ( K == S ) {
		bool space = false;
		for (int i = 1; i<= S; i++) {
			if ( space ) printf(" ");
			else space = true;
			printf("%d", i);
		}
		printf("\n");
		return;
	}
	printf("\n");
	return;
}

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1; i<=t; i++) {
		Read(i);
		Solve();
	}
	return 0;
}
