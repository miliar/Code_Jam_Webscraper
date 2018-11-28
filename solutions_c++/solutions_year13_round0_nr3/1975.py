#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;


vector<unsigned long long> tab;



unsigned long long rev(unsigned long long v) {
    unsigned long long v1=0ll;
    while (v) {
	v1*=10;
	v1+=v%10;
	v/=10;
    }
    return v1;
}

bool ifpoli(unsigned long long v) {
    return v==rev(v);
}



void gentab() {
    for (unsigned long long v=0ll; v<10000000ll; v++) {
	if (ifpoli(v)) if (ifpoli(v*v)) tab.push_back(v*v);
    }
}



int main() {
    int T;
    scanf("%d", &T);
    gentab();
    for (int t=1; t<=T; t++) {
	unsigned long long A, B;
	scanf ("%lld %lld", &A, &B);
	int W=upper_bound(tab.begin(), tab.end(), B)-lower_bound(tab.begin(), tab.end(), A);
	
        printf("Case #%d: %d\n", t, W);
    }
    return 0;
}

