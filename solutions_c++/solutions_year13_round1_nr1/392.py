#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

typedef long long LL;
#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int main() {
    int testCase;
    scanf("%d", &testCase);
    for (int _tests = 1; _tests <= testCase; _tests++) {
        printf("Case #%d: ",_tests);
        LL r, t;
        cin>>r>>t;
        LL low = 0, high = t/r/2, mid;
        while (low < high) {
            mid = (high + low + 1)/2;
            LL val = (1 + 2 * r) * (mid + 1);
            if (val > t || (mid >= 2000000000LL)) {
                high = mid - 1;
                continue;
            }
            if (mid * (mid - 1) > t) {
                high = mid - 1;
                continue;
            }
            val += 2 * mid * (mid + 1);
            //cout<<low<<" "<<high<<" "<<mid<<" "<<val<<"\n";
            if (val > t) high = mid - 1;
            else low = mid;
        }
        cout<<low+1<<"\n";;
    }
	return 0;
}
