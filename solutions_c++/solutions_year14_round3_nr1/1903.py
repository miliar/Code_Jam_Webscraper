#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

void solve(int id) {
	// local variables
    int p,q;
	// read data
    scanf_s("%d/%d", &p, &q);
    if (q &(-q) != q) { 
        printf("Case #%d: impossible\n", id); 
        return;
    }
	// process
    int g = 0;
    while (p < q) {
        g++;
        p = p<<1;
    }
	// output
	printf("Case #%d: %d\n", id, g > 0 ? g:1);
}

int main(int argc, char *argv[]) {
	int t = 0;
	cin>>t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
}
