#include <bits/stdc++.h>
using namespace std;

// true se for sempre possivel formar
// false do contrario
bool run() {
    int x, r, c;
    cin>>x>>r>>c;
    if (r > c) swap(r, c);
    const int area = r*c;

    // r <= c
    if (x <= c && (area % x) == 0) {
        if (x == 1) {
            return true;
        } else if (x == 2) {
            // 1x2 or 2x2 (OK) or 2x3 (OK) or 2x4 (OK) or 3x3 (IMP) or 3x4 (OK) or 4x4 (OK)
            return true;
        } else if (x == 3) {
            // 1x3 (NO) 2x3 (OK) or 2x4 (IMP) or 3x3 (OK) or 3x4 (OK) or 4x4 (IMP) -- OK
            return r != 1;
        } else if (x == 4) {
            // 1x4 (NO) or 2x4 (NO) or 3x4 (OK) or 4x4 (OK*)
            return r != 1 && r != 2;
        } else {
            throw 42;
        }
    } else {
        return false;
    }
}

int main() {
	int tests;
	cin>>tests;
	for (int test = 1; test <= tests; ++test) {
	    cout<<"Case #"<<test<<": ";
	    cout<<(run() ? "GABRIEL" : "RICHARD");
	    cout<<"\n";
	}
}