#include <cstdio>
#include <algorithm>
using namespace std;
double a[1003], b[1003];

// 0.186000 0.300000 0.389000 0.557000 0.832000 0.899000 0.907000 0.959000 0.992000 
// 0.215000 0.271000 0.341000 0.458000 0.520000 0.521000 0.700000 0.728000 0.916000
int deceitful_war(int n) {
    int ans=0;
    for (int i=0,j=0; i<n; ++i)
        if (a[i]>b[j]) ++j, ++ans;
    return ans;
}

int war(int n) {
    int ans=0;
    for (int i=n-1, j=n-1; i>=0; --i) {
        if (a[i]>b[j]) ++ans;
        else --j;
    }
    return ans;
}

int main() {
    int casenum; scanf("%d", &casenum);
    for (int casei=1; casei<=casenum; ++casei) {
        int n; scanf("%d", &n);
        for (int i=0; i<n; ++i) scanf("%lf", &a[i]);
        for (int i=0; i<n; ++i) scanf("%lf", &b[i]);
        sort(a, a+n);
        sort(b, b+n);
        printf("Case #%d: %d %d\n", casei, deceitful_war(n), war(n));
    }
    return 0;
}
