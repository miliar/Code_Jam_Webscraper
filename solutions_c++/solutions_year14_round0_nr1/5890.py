#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>

#define ll long long

using namespace std;

int d, zt;
int main() {
    scanf("%d", &zt);
    
    for (int kt=0; kt<zt; ++kt) {
	int a[4], b[4], c[4];
	scanf("%d", &d);
	
	for (int i=0; i<4; ++i) {
	    for (int j=0; j<4; ++j) {
		scanf("%d", &a[j]);
		if (i+1 == d) b[j] = a[j];
	    }
	}
	scanf("%d", &d);
	
	for (int i=0; i<4; ++i) {
	    for (int j=0; j<4; ++j) {
		scanf("%d", &a[j]);
		if (i+1 == d) c[j] = a[j];
	    }
	}
	int r = -1;
	
	for (int i=0; i<4; ++i) {
	    for (int j=0; j<4; ++j) {
		if (c[i] == b[j]) {
		    r = (r == -1 ? c[i] : -2);
		}
	    }
	}
	
	if (r >= 0) printf("Case #%d: %d\n", kt+1, r);
	else printf("Case #%d: %s\n", kt+1, (r == -2 ? "Bad magician!" : "Volunteer cheated!"));
    }
}