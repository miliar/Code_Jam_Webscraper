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
#include <queue>


using namespace std;

int D;
int P[1005];


bool possible(int k) {
    // Is it possible in time k?
    
    // Cycle over h (number of splittings)
    for (int h=0; h<k; h++) {
        
        if (D == 0) return 1;
        int time = k-h;
        
        int used = 0;
        for (int i=D-1; i>=0; i--) {
            int x = P[i];
            used += ((x+time-1) / time) - 1;
            if (used > h) break;
        }
        
        if (used <= h) return 1;
    }
    
    return 0;
}

int binary_search(int a, int b) {
    if (a == b) return a;
    
    int m = (a+b)/2;
    
    
    if (possible(m)) {
        return binary_search(a,m);
    }
    else {
        return binary_search(m+1,b);
    }
}


void solve() {
	scanf("%d", &D);
	for (int i=0; i<D; i++) {
	    scanf("%d", P+i);
	}
	
	sort(P, P+D);
	
	printf("%d\n", binary_search(0,1000));
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
