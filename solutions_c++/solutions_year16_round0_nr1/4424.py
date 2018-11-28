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

int n;
bool f[10];

void Read() {
	scanf("%d",&n);
	memset(f,0,10);
	return;
}

void mod ( int c ) {
	while ( c ) {
		f[c%10] = true;
		//printf("%d %d\n", c%10, c);
		c/=10;
	}
}

bool check() {
	for (int i=0; i<=9; i++) {
		if ( !f[i] ) return false;
	}
	return true;
}

void Solve() {
	if ( n == 0 ) {
		printf("INSOMNIA\n");
		return;
	}
	int c = n;
	while (1) {
		mod(c);
		if ( check() ) {
			printf("%d\n", c);
			return;
		}
		c += n;
	}
	return;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i = 1; i<=t; i++) {
		Read();
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
