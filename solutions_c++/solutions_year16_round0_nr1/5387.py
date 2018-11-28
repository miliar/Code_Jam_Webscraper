#include<bits/stdc++.h>
using namespace std;

set<int> mys;
void solve(int n) {
    mys.clear();
    long long int n1, n2;
    for(int i = 1; i <= 100000; i++) {
        n1 = i*n;
        n2 = n1;
        while(n1) {
            int k = n1%10;
            mys.insert(k);
            n1 = n1/10;
        }
        if(mys.size() == 10) {
                printf("%lld\n",n2);
                break;
        }
    }
    if(mys.size()<10) {
        printf("INSOMNIA\n");
    }
    return;
}
int main() {
    int tc, n, ans;
    scanf("%d", &tc);
    int k = 1;
    while(tc--) {
        scanf("%d", &n);
        printf("Case #%d: ",k++);
        solve(n);
    }
    return 0;
}

