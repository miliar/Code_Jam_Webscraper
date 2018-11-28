#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <set>
#include <map>


using namespace std;

int n;
pair<int,int> a[10000];


int tree[10000];

// Returns sum of elements with indexes a..b, inclusive
int query(int a, int b) {
    if (a == 0) {
        int sum = 0;
        for (; b >= 0; b = (b & (b + 1)) - 1)
          sum += tree[b];
        return sum; 
    } else {
        return query(0, b) - query(0, a-1);
    }
}

// Increases value of k-th element by inc.
void increase(int k, int inc) {
    for (; k < n; k |= k + 1)
        tree[k] += inc;
}





void solve() {
	scanf("%d", &n);
	for (int i=0; i<n; i++) {
		int val;
		scanf("%d", &val);
		a[i] = pair<int,int>(val, i);
		
		tree[i] = 0;
	}
	
	for (int i=0; i<n; i++) {
		increase(i, 1);
	}
	
	sort(a, a+n);
	/*
	for (int i=0; i<n; i++) {
		printf("Val: %d. Pos: %d\n", a[i].first, a[i].second);
	}
	*/
	
	int sol = 0;
	
	for (int i=0; i<n; i++) {
		int pos = a[i].second;
		//printf("Processo %d. Costi: %d, %d\n", i, query(0,pos-1), query(pos+1,n-1));
		int cost = min( query(0,pos-1), query(pos+1,n-1) );
		sol += cost;
		increase(pos,-1);
	}
	
	printf("%d\n", sol);
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
