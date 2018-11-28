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

int len;
char pan[105];

void Read() {
	scanf("%s",pan);
	len = strlen(pan);
	return;
}

void Solve() {
	int g = 1;
	for (int i=0; i<len-1; i++) {
		if ( pan[i] != pan[i+1] ) g++;
	}
	if ( pan[len-1] == '+' ) printf("%d\n", g-1);
	else printf("%d\n", g);
	return;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1; i<=t; i++) {	
		Read();
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
